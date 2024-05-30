# End to End ML Project

# Deployment steps: AWS CICD-Deployment with Github Actions

1. Login to AWS Console
2. Create IAM user for deployment

# with specific acess
1. EC2 access: It is virtual machine
2. ECR: Elastic Container Registry to save your docker image in aws

# Description about the deployment
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch your EC2
4. Pull your image from ECR in EC2
5. Launch your docker image in EC2

# Policy
1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

3. Create ECR repo to store/save docker image
 - save the URI: 767397810021.dkr.ecr.ap-southeast-2.amazonaws.com/mlproject

4. Create EC2 machine (ubuntu)

5. Open EC2 and install docker in EC2 Machine

#optional
sudo apt-get update -y
sudo apt-get upgrade
#required
curl 0fs5L https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

6. Configure EC2 as self hosted runner
setting>actions>runner>new self hosted runner> choose os>then run command one by one

7. Setup github secrets
AWS_ACCESS_KEY_ID = 
AWS_SECRET_ACCESS_KEY = 
AWS_REGION = us-east-1
AWS_ECR_LOGIN_URI = demo>
ECR_REPOSITORY_NAME = simple-app

