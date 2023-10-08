This 3-tier environment includes a VPC (Virtual Private Cloud), web servers in a public subnet, application servers in a private subnet, and a database server in another private subnet.
It uses the aws terraform provider and assumes that the aws cli is installed, and valid credentials are present under `~/.aws/credentials`

To execute:
```
cd terraform
terraform init
terraform apply
```
