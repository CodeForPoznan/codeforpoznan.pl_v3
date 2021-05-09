#!/usr/bin/env bash
set -Eeuo pipefail


case "${1:-}" in
  staging)
    echo "deploying to staging"
    export RESOURCE="${STAGING_RESOURCE}"
    export AWS_ACCESS_KEY_ID="${STAGING_AWS_ACCESS_KEY_ID}"
    export AWS_SECRET_ACCESS_KEY="${STAGING_AWS_SECRET_ACCESS_KEY}"
  ;;

  production)
    echo "deploying to production"
    export RESOURCE="${PRODUCTION_RESOURCE}"
    export AWS_ACCESS_KEY_ID="${PRODUCTION_AWS_ACCESS_KEY_ID}"
    export AWS_SECRET_ACCESS_KEY="${PRODUCTION_AWS_SECRET_ACCESS_KEY}"
  ;;

  *)
    echo "invalid environment '${1}', exiting..."
    exit 1
  ;;
esac


echo "build and push frontend"
(cd frontend && yarn run build && cp -r dist ../public)
aws s3 sync --delete public "s3://codeforpoznan-public/${RESOURCE}"


echo "refresh CDN"
dist_id=$(
  aws cloudfront list-distributions \
    | jq --arg PATH "/${RESOURCE}" -r '
      .DistributionList.Items[]
      | {Id, p: .Origins.Items[].OriginPath}
      | select(.p == $PATH).Id'
)
aws cloudfront create-invalidation --paths "/*" --distribution-id "${dist_id}"


echo "bundle application"
(cd backend  && pipenv run pip install -r <(pipenv lock -r) --target ../packages)
(cd packages && zip -qgr9 ../lambda.zip .)
ln  --symbolic backend/migrations migrations
zip --symlinks -qgr9 lambda.zip backend/ migrations/


echo "upload lambdas"
aws s3 cp lambda.zip "s3://codeforpoznan-lambdas/${RESOURCE}_serverless_api.zip"
aws s3 cp lambda.zip "s3://codeforpoznan-lambdas/${RESOURCE}_migration.zip"


echo "refresh lambdas"
aws lambda update-function-code                           \
  --s3-bucket     "codeforpoznan-lambdas"                 \
  --s3-key        "${RESOURCE}_serverless_api.zip"        \
  --function-name "${RESOURCE}_serverless_api"            \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)' \

aws lambda update-function-code                           \
  --s3-bucket     "codeforpoznan-lambdas"                 \
  --s3-key        "${RESOURCE}_migration.zip"             \
  --function-name "${RESOURCE}_migration"                 \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)' \


echo "run migrations"
aws lambda invoke                         \
  --function-name "${RESOURCE}_migration" \
  response.json                           \
> request.json                            \


echo "show migration output"
jq -s add ./*.json | jq -re '
  if .FunctionError then
    .FunctionError, .errorMessage, false
  else
    .stdout, .stderr
  end'


exit $?
