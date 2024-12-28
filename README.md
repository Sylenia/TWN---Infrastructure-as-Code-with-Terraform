# Modularize Project

## Overview
This project demonstrates how to modularize a Terraform configuration into reusable components. Modularizing your infrastructure code improves maintainability, scalability, and reusability. In this project, the `main.tf` file was divided into modules to manage different AWS resources like VPCs, subnets, and EC2 instances.

## Technologies Used
- **Terraform**
- **AWS**
- **Docker**
- **Linux**
- **Git**

## Project Description
The project modularizes Terraform resources into reusable components to better manage infrastructure as code. Each module encapsulates a specific part of the infrastructure, such as subnets, VPCs, and web servers, ensuring clean separation of concerns.

---

## File Structure

```plaintext
.
├── main.tf
├── modules
│   ├── subnet
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── variables.tf
│   │   └── providers.tf
│   ├── webserver
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── variables.tf
│   │   └── providers.tf
├── variables.tf
├── outputs.tf
├── provider.tf
```

---

## Step-by-Step Guide to Modularize a Terraform Project

### Step 1: Initialize the Project
1. Install Terraform: [Download Terraform](https://www.terraform.io/downloads)
2. Create a project directory:
   ```bash
   mkdir terraform-modular-project
   cd terraform-modular-project
   ```
3. Initialize a Git repository:
   ```bash
   git init
   ```
4. Create a `main.tf` file and configure your AWS provider:
   ```hcl
   provider "aws" {
     region = "eu-central-1"
   }
   ```

### Step 2: Define Modules
#### Create a VPC Module
1. Create a `modules/vpc` directory:
   ```bash
   mkdir -p modules/vpc
   ```
2. Define the `main.tf` file for the VPC module:
   ```hcl
   resource "aws_vpc" "myapp-vpc" {
     cidr_block = var.vpc_cidr_blocks
     tags = {
       Name = "${var.env_prefix}-vpc"
     }
   }
   ```
3. Add `variables.tf`:
   ```hcl
   variable "vpc_cidr_blocks" {}
   variable "env_prefix" {}
   ```
4. Add `outputs.tf`:
   ```hcl
   output "vpc_id" {
     value = aws_vpc.myapp-vpc.id
   }
   ```

#### Create a Subnet Module
1. Repeat the above steps for the subnet module in `modules/subnet`:
   ```hcl
   resource "aws_subnet" "myapp-subnet-1" {
     vpc_id = var.vpc_id
     cidr_block = var.subnet_cidr_blocks
     availability_zone = var.avail_zone
     tags = {
       Name = "${var.env_prefix}-subnet-1"
     }
   }
   ```

### Step 3: Use Modules in `main.tf`
Define modules in your main `main.tf` file:
```hcl
module "myapp-subnet" {
  source = "./modules/subnet"
  subnet_cidr_blocks = var.subnet_cidr_blocks
  avail_zone = var.avail_zone
  env_prefix = var.env_prefix
  vpc_id = module.myapp-vpc.vpc_id
}

module "myapp-server" {
  source = "./modules/webserver"
  avail_zone = var.avail_zone
  env_prefix = var.env_prefix
  vpc_id = module.myapp-vpc.vpc_id
  my_ip = var.my_ip
  image_name = var.image_name
  public_key_location = var.public_key_location
  instance_type = var.instance_type
  subnet_id = module.myapp-subnet.subnet_id
}
```

### Step 4: Initialize and Apply Terraform Configuration
1. Initialize Terraform:
   ```bash
   terraform init
   ```
2. Validate the configuration:
   ```bash
   terraform validate
   ```
3. Plan the deployment:
   ```bash
   terraform plan
   ```
4. Apply the configuration:
   ```bash
   terraform apply
   ```

---

## Best Practices

1. **Use Variables:** Define variables in `variables.tf` for better flexibility.
2. **Use Outputs:** Export essential resource attributes with `outputs.tf`.
3. **State Management:** Use a remote backend like S3 to store the Terraform state securely.
4. **Version Control:** Commit changes incrementally and use branches for features.
5. **Consistent Naming:** Use a consistent naming convention for resources and variables.

---

## Example Commands

1. Initialize Terraform:
   ```bash
   terraform init
   ```
2. Plan deployment:
   ```bash
   terraform plan
   ```
3. Apply deployment:
   ```bash
   terraform apply
   ```
4. Destroy resources:
   ```bash
   terraform destroy
   ```

---

## Sum
Modularizing your Terraform configurations helps manage complex infrastructure efficiently. This project provides a clear example of how to divide Terraform code into reusable modules for scalability and ease of maintenance.

