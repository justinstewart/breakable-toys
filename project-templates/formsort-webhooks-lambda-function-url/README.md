# Formsort Webhooks w/ AWS Lambda function URLs
This is an AWS SAM project that deploys a Lambda function URL as a Formsort webhook integration.

## Development
```shell
docker-compose build
docker-compose run tests
```

## Deployment
This project requires an ECR repository for storing the Lambda images and the SAM CLI for deployment.

```shell
sam build
sam deploy --stack-name ${STACK_NAME} \
           --image-repository ${IMAGE_REPO} \
           --capabilities CAPABILITY_NAMED_IAM
```
