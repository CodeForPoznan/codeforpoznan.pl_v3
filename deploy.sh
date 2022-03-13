#!/usr/bin/env bash
set -Eeuo pipefail


# run only if frontend artifact is avaiable
if [ -d "public" ]; then

  echo "push frontend"
  aws s3 sync                                \
    --delete public                          \
    "s3://codeforpoznan-public/${RESOURCE}"  \


  echo "refresh CDN"
  aws cloudfront create-invalidation         \
    --paths "/*"                             \
    --distribution-id "${AWS_CLOUDFRONT_ID}" \

fi


# run only if backend artifact is avaiable
if [ -f "lambda.zip" ]; then

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

fi


exit $?
