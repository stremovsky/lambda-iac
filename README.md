# Sample Lambda / API Gateway / DynamoDB Project Created with Terraform

## Prerequisites
1. Download and install [Terraform](https://developer.hashicorp.com/terraform/install)
2. Ensure you have AWS CLI installed and configured with appropriate access keys

## How to use
1. Modify ``provider.tf`` file to ensure Terraform can work with your AWS access key. For example, you might use a custom AWS profile.
2. Install Terraform dependencies with ``terraform init`` command.
3. Run the ``./prepare-files.sh`` script to zip Python script files. script to zip python script files. The files will be saved into the hidden ``./files`` directory.
4. Run ``terraform apply`` to create all AWS infrastructure for this project: Lambda functions, API Gateway, and DynamoDB table.
5. Run ``./test-api-gw.sh`` to create a record in DynamoDB, dump it, and remove it.
6. Destroy infrustreucture with ``terraform destroy``

## All the steps together except the first one:
```
terraform init
./prepare-files.sh
terraform apply -auto-approve
./test-api-gw.sh
terraform destroy -auto-approve
```
