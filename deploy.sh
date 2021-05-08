#!/usr/bin/env bash
set -Eeuo pipefail


resource="${1:-dev_codeforpoznan_pl_v3}"


echo "deploying to '${resource}'"
[[ "${resource}" ]] || exit 1


echo "build and push frontend"
(cd frontend && yarn run build && cp -r dist ../public)
aws s3 sync --delete public "s3://codeforpoznan-public/${resource}"


echo "refresh CDN"
dist_id=$(
  aws cloudfront list-distributions \
    | jq --arg PATH "/$resource" -r '
      .DistributionList.Items[]
      | {Id, p: .Origins.Items[].OriginPath}
      | select(.p == $PATH).Id'
)
aws cloudfront create-invalidation --paths "/*" --distribution-id "$dist_id"


echo "bundle application"
(cd backend && pipenv run pip install -r <(pipenv lock -r) --target ../packages)
(cd packages && zip -qgr9 ../lambda.zip .)
ln -s backend/migrations migrations
zip --symlinks -qgr9 lambda.zip backend/ migrations/


echo "upload lambdas"
aws s3 cp lambda.zip "s3://codeforpoznan-lambdas/${resource}_serverless_api.zip"
aws s3 cp lambda.zip "s3://codeforpoznan-lambdas/${resource}_migration.zip"


echo "refresh lambdas"
aws lambda update-function-code                           \
  --function-name "${resource}_serverless_api"            \
  --s3-bucket     "codeforpoznan-lambdas"                 \
  --s3-key        "${resource}_serverless_api.zip"        \
  --region        "eu-west-1"                             \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)' \

aws lambda update-function-code                           \
  --function-name "${resource}_migration"                 \
  --s3-bucket     "codeforpoznan-lambdas"                 \
  --s3-key        "${resource}_migration.zip"             \
  --region        "eu-west-1"                             \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)' \


echo "run migrations"
aws lambda invoke                         \
  --function-name "${resource}_migration" \
  --region        "eu-west-1"             \
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
