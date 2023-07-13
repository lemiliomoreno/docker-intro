Commands:

1. Run:

```bash
docker compose up -d
```

2. Stop

```bash
docker compose stop
```

To push image to ECR:

1. Set your AWS environment variables to log into AWS (check if `aws sts get-caller-identity` commandd works)

2. Push your image to ECR:

Linux

```bash
export AWS_ACCOUNT_ID=<AWS_ACCOUNT_ID>
export AWS_DEFAULT_REGION=us-west-2
export AWS_ECR_REPOSITORY_NAME=academia
export DOCKER_IMAGE_TAG=latest

aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
docker build -t sample-compose:${DOCKER_IMAGE_TAG} .
docker tag sample-compose:${DOCKER_IMAGE_TAG} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${AWS_ECR_REPOSITORY_NAME}:${DOCKER_IMAGE_TAG}
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${AWS_ECR_REPOSITORY_NAME}:${DOCKER_IMAGE_TAG}
```

Windows

```bat
set AWS_ACCOUNT_ID=<AWS_ACCOUNT_ID>
set AWS_DEFAULT_REGION=us-west-2
set AWS_ECR_REPOSITORY_NAME=academia
set DOCKER_IMAGE_TAG=latest

aws ecr get-login-password --region %AWS_DEFAULT_REGION% | docker login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_DEFAULT_REGION%.amazonaws.com
docker build -t sample-compose:%DOCKER_IMAGE_TAG% .
docker tag sample-compose:%DOCKER_IMAGE_TAG% %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_DEFAULT_REGION%.amazonaws.com/%AWS_ECR_REPOSITORY_NAME%:%DOCKER_IMAGE_TAG%
docker push %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_DEFAULT_REGION%.amazonaws.com/%AWS_ECR_REPOSITORY_NAME%:%DOCKER_IMAGE_TAG%
```

3. Deploy to AWS
```bash
docker context create ecs academia

# Select - AWS environment variables
Docker Compose's integration for ECS and ACI will be retired in November 2023. Learn more: https://docs.docker.com/go/compose-ecs-eol/
? Create a Docker context using:  [Use arrows to move, type to filter]
  An existing AWS profile
  AWS secret and token credentials
> AWS environment variables

docker context use academia

docker compose -f docker-compose.yml -f docker-compose.prod.yml up
```

Troubleshoot if any errors:

```bash
docker --context default context use default
```
