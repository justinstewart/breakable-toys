# Base SAM Python Project
This is a basic SAM Python project that utilizes Docker based images for Lambda.

## Development
```shell
docker-compose build
docker-compose run tests
```

## Deployment
This project requires an ECR repository for storing the Lambda images.

```shell
sam build
sam deploy --stack-name ${STACK_NAME} \
           --image-repository ${IMAGE_REPO} \
           --capabilities CAPABILITY_NAMED_IAM
```
