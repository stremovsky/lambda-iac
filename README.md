# Sample Lambda / API Gateway / DynamoDB Project Created with Terraform

## Prerequisites
1. Download and install [Terraform](https://developer.hashicorp.com/terraform/install)
2. Ensure you have AWS CLI installed and configured with appropriate access keys

## How to use
1. Install Terraform dependencies with ``terraform init`` command.
2. Run the ``./prepare-files.sh`` script to zip Python script files. The files will be saved into the hidden ``./files`` directory.
3. Run ``terraform apply`` to create all AWS infrastructure for this project: Lambda functions, API Gateway, and DynamoDB table.
4. Run ``./test-api-gw.sh`` to create a record in DynamoDB, dump it, and remove it.
5. Destroy infrastructure with ``terraform destroy``

## All the steps together except the first one:

```
# Change AWS profile and region to the one you use
export AWS_PROFILE='default'
export AWS_REGION='us-east-1'
terraform init
./prepare-files.sh
terraform apply -auto-approve
./test-api-gw.sh
terraform destroy -auto-approve
```
