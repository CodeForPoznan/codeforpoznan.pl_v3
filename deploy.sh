#!/usr/bin/env bash

echo "build and push frontend"
(cd frontend && yarn run build && cp -r dist ../public)
aws s3 sync --delete public s3://codeforpoznan-public/dev_codeforpoznan_pl_v3
aws cloudfront create-invalidation --paths "/*" --distribution-id E6PZCV3N5WWJ8

echo "bundle application"
pipenv run pip install -r <(pipenv lock -r) --target packages
(cd packages && zip -qgr9 ../lambda.zip .)
ln -s backend/migrations migrations
zip --symlinks -qgr9 lambda.zip backend/ migrations/

echo "upload lambdas"
aws s3 cp lambda.zip s3://codeforpoznan-lambdas/dev_codeforpoznan_pl_v3_serverless_api.zip
aws s3 cp lambda.zip s3://codeforpoznan-lambdas/dev_codeforpoznan_pl_v3_migration.zip

echo "refresh lambdas"
aws lambda update-function-code                              \
  --function-name dev_codeforpoznan_pl_v3_serverless_api     \
  --s3-bucket     codeforpoznan-lambdas                      \
  --s3-key        dev_codeforpoznan_pl_v3_serverless_api.zip \
  --region        eu-west-1                                  \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)'    \

aws lambda update-function-code                              \
  --function-name dev_codeforpoznan_pl_v3_migration          \
  --s3-bucket     codeforpoznan-lambdas                      \
  --s3-key        dev_codeforpoznan_pl_v3_migration.zip      \
  --region        eu-west-1                                  \
| jq 'del(.Environment, .VpcConfig, .Role, .FunctionArn)'    \

echo "run migrations"
aws lambda invoke                                            \
  --function-name dev_codeforpoznan_pl_v3_migration          \
  --region        eu-west-1                                  \
  response.json                                              \
> request.json                                               \

echo "show migration output"
jq -s add ./*.json | jq -re '
  if .FunctionError then
    .FunctionError, .errorMessage, false
  else
    .stdout, .stderr
  end'

exit $?
