# Using Terraform Provisioners: Updated Demo Project

This README reflects changes made to the `main.tf` file to include **Terraform provisioners** for configuring and managing resources. Additionally, it explains when to use provisioners, their drawbacks, and why tools like **Ansible** are preferred for provisioning tasks.

---

## Table of Contents
1. [What Are Terraform Provisioners?](#what-are-terraform-provisioners)
2. [When to Use Provisioners](#when-to-use-provisioners)
3. [Why Provisioners Are Not Recommended](#why-provisioners-are-not-recommended)
4. [Best Practices for Resource Provisioning](#best-practices-for-resource-provisioning)
5. [Updated Project Features](#updated-project-features)
6. [Step-by-Step Guide](#step-by-step-guide)

---

## What Are Terraform Provisioners?
Provisioners in Terraform allow you to execute scripts or commands on a resource after it is created or before it is destroyed. They are often used to configure resources or run necessary setup tasks directly from Terraform.

Terraform supports three main types of provisioners:
- **File Provisioner**: Transfers files to a remote resource.
- **Remote-Exec Provisioner**: Executes remote scripts or commands via SSH.
- **Local-Exec Provisioner**: Executes local scripts or commands on the machine running Terraform.

---

## When to Use Provisioners
You should only use provisioners when:
1. There is no other way to achieve the desired configuration using resource attributes or modules.
2. The provisioning logic is simple, and no complex orchestration is required.
3. Temporary tasks are required, such as debugging or generating output files (e.g., `local-exec`).

Examples from this project:
- **File Provisioner**: Copies the `entry-script.sh` to the EC2 instance.
- **Remote-Exec Provisioner**: Executes the `entry-script.sh` script to configure Docker and NGINX on the instance.
- **Local-Exec Provisioner**: Outputs the EC2 public IP to a local file for easy reference.

---

## Why Provisioners Are Not Recommended
### 1. **Provisioners Break Declarative Infrastructure**
Terraform is designed as a declarative tool, meaning you define the desired state of your infrastructure, and Terraform ensures it is achieved. Provisioners introduce imperative behavior, which can lead to:
   - Lack of idempotence: Scripts may fail if re-run or executed multiple times.
   - Dependency issues: Failures in provisioners can leave resources in an inconsistent state.

### 2. **Error Handling is Limited**
If a provisioner fails, Terraform stops the apply process and does not roll back. This can leave your infrastructure in a partially provisioned state.

### 3. **Better Alternatives Exist**
Tools like **Ansible**, **Chef**, or **Puppet** are designed specifically for provisioning and configuration management. These tools:
   - Provide robust error handling.
   - Allow for better modularity and reuse of scripts.
   - Offer agentless configuration (e.g., Ansible over SSH).

---

## Best Practices for Resource Provisioning
1. **Use Cloud-Native Features**: Use native AWS services like **AWS User Data** for simple EC2 configuration.
2. **Leverage Configuration Management Tools**: Use tools like **Ansible** to manage provisioning outside Terraform.
3. **Minimize Provisioner Usage**: Only use provisioners for tasks that cannot be handled natively by Terraform.

---

## Updated Project Features
1. **Infrastructure Components**:
   - VPC, Subnet, Route Table, Internet Gateway, Security Group, and EC2 Instance.
2. **Provisioners**:
   - `File Provisioner`: Transfers the setup script to the EC2 instance.
   - `Remote-Exec Provisioner`: Runs the setup script to install Docker and NGINX.
   - `Local-Exec Provisioner`: Outputs the EC2 instance's public IP to a local file.

---

## Step-by-Step Guide

### Step 1: Update `terraform.tfvars`
Ensure your variable file is updated with valid example values:

```hcl
vpc_cidr_blocks = "10.0.0.0/16"
subnet_cidr_blocks = "10.0.10.0/24"
env_prefix = "dev"
avail_zone = "eu-central-1b"
my_ip = "203.0.113.42/32"  # Replace with your public IP
instance_type = "t2.micro"
public_key_location = "C:/path/to/your/public_key.pub"
private_key_location = "C:/path/to/your/private_key.pem"
```

### Step 2: Initialize Terraform
Run the following command to initialize Terraform:

```bash
terraform init
```

### Step 3: Validate and Apply the Configuration
Validate the configuration:

```bash
terraform validate
```

Apply the configuration:

```bash
terraform apply
```

Review the plan and type `yes` to confirm.

### Step 4: Verify Provisioners
1. Check the EC2 instance to ensure the file is present:
   ```bash
   ssh -i "path/to/your/private_key.pem" ec2-user@<EC2_PUBLIC_IP>
   ls /home/ec2-user/entry-script-on-ec2.sh
   ```

2. Ensure the script has been executed (Docker and NGINX installed):
   ```bash
   docker ps
   curl http://<EC2_PUBLIC_IP>:8080
   ```

3. Confirm the local file contains the EC2 public IP:
   ```bash
   cat output.txt
   ```

---

## Sum
While provisioners can be helpful for simple or temporary tasks, they should not be your default choice for provisioning. For robust and scalable solutions, leverage dedicated configuration management tools like **Ansible**, which complement Terraform's declarative nature without sacrificing idempotence or error handling.
