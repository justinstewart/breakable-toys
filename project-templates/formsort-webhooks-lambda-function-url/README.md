# Formsort Webhooks w/ AWS Lambda function URLs
This is an AWS SAM project that deploys a Lambda function URL as a Formsort webhook integration.

## Development
```shell
docker-compose build
docker-compose run tests
```

## Deployment
This project requires an ECR repository for storing the Lambda images and the SAM CLI for deployment. Make sure your SAM CLI is updated to take advantage of Lambda function URLs.

You'll also need a signing key from Formsort. This can be obtained when you [setup your webhook integration](https://docs.formsort.com/handling-data/integration-reference/webhooks#setting-up-the-webhook-integration).

```shell
sam build
sam deploy --stack-name ${STACK_NAME} \
           --image-repository ${IMAGE_REPO} \
           --capabilities CAPABILITY_NAMED_IAM \
           --parameter-overrides SigningKey=${SIGNING_KEY}
```

> Note: For simplicity, we pass the signing key directly to our CloudFormation template. However, in a production environment, this should be considered a secret. Our recommendation is to add your signing key to Secrets Manager and tweak the template SigningKey parameter to use it as its source.
