# Demo Project: Automate AWS Infrastructure

This project demonstrates how to use **Terraform**, **AWS**, and **Docker** to automate provisioning AWS infrastructure and deploy a Docker container on an EC2 instance. It creates essential components like a VPC, Subnet, Route Table, Internet Gateway, Security Group, and EC2 instance.

---

## Table of Contents
1. [Technologies Used](#technologies-used)
2. [Project Features](#project-features)
3. [Setup and Prerequisites](#setup-and-prerequisites)
4. [Step-by-Step Guide](#step-by-step-guide)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Configure Terraform Variables](#step-2-configure-terraform-variables)
   - [Step 3: Initialize Terraform](#step-3-initialize-terraform)
   - [Step 4: Validate the Configuration](#step-4-validate-the-configuration)
   - [Step 5: Apply Terraform Plan](#step-5-apply-terraform-plan)
   - [Step 6: Access the Deployed Application](#step-6-access-the-deployed-application)
5. [File Structure](#file-structure)
6. [License](#license)

---

## Technologies Used
- **Terraform** (Version 1.5 or later)
- **AWS** (Infrastructure as a Service provider)
- **Docker** (Containerization tool)
- **Linux** (Instance operating system)
- **Git** (Version control)

---

## Project Features
1. Automates the provisioning of AWS infrastructure components, including:
   - VPC
   - Subnet
   - Route Table
   - Internet Gateway
   - Security Group
   - EC2 Instance
2. Deploys an NGINX Docker container to the EC2 instance automatically.

---

## Setup and Prerequisites

Before you begin, ensure you have:
1. **AWS Account** with programmatic access and necessary permissions.
2. **Terraform** installed on your machine. [Download Terraform](https://www.terraform.io/downloads.html)
3. **AWS CLI** installed and configured. [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
4. **Git** installed. [Install Git](https://git-scm.com/)
5. SSH key pair generated for accessing the EC2 instance.

---

## Step-by-Step Guide

### Step 1: Clone the Repository
Clone this project repository to your local machine:

```bash
git clone <repository_url>
cd <repository_name>
```

### Step 2: Configure Terraform Variables
Edit the `terraform.tfvars` file with your own values. Use the following example values:

```hcl
vpc_cidr_blocks = "10.0.0.0/16"
subnet_cidr_blocks = "10.0.10.0/24"
env_prefix = "dev"
avail_zone = "eu-central-1b"
my_ip = "203.0.113.42/32"  # Replace with your public IP
instance_type = "t2.micro"
public_key_location = "C:/path/to/your/public_key.pub"
```

> **Note**: Replace `public_key_location` with the full path to your SSH public key.

### Step 3: Initialize Terraform
Run the following command to initialize Terraform and download necessary providers:

```bash
terraform init
```

### Step 4: Validate the Configuration
Validate your Terraform scripts to ensure correctness:

```bash
terraform validate
```

### Step 5: Apply Terraform Plan
Run the following command to deploy the infrastructure:

```bash
terraform apply
```

Review the plan and type `yes` to confirm.

### Step 6: Access the Deployed Application
Once the deployment is complete:
1. Note the EC2 instance's public IP from the output.
2. SSH into the instance:

   ```bash
   ssh -i "path/to/your/private_key.pem" ec2-user@<EC2_PUBLIC_IP>
   ```

3. Open a browser and navigate to `http://<EC2_PUBLIC_IP>:8080` to view the NGINX default page.

---

## File Structure

```plaintext
.
├── main.tf            # Main Terraform configuration file
├── providers.tf       # Provider configuration
├── terraform.tfvars   # User-defined variables
├── entry-script.sh    # Script to install Docker and run NGINX
├── README.md          # Project documentation
```

---


