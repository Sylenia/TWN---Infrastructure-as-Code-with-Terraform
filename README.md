# Terraform & AWS EKS: Automated Deployment

## Overview
This demo project showcases how to automate the provisioning of an AWS Elastic Kubernetes Service (EKS) cluster using Terraform. The project is designed for DevOps learners who want to explore infrastructure as code (IaC) to streamline deployment and management of cloud resources.

## Technologies Used
- **Terraform**: Infrastructure as Code (IaC) tool for provisioning and managing cloud resources.
- **AWS EKS**: Managed Kubernetes service by AWS.
- **Docker**: For containerized deployments.
- **Linux**: Operating system for local development.
- **Git**: Version control system.

---

## Project Description
This project automates the deployment of an EKS cluster, complete with necessary networking components, using Terraform. The configuration files include:

- **`vpc.tf`**: Defines the VPC, subnets, and related networking resources.
- **`eks-cluster.tf`**: Configures the EKS cluster and node groups.
- **`providers.tf`**: Specifies AWS as the provider.
- **`.tfvars`**: Stores variable values for customization.

---

## Concepts Explained
1. **Infrastructure as Code (IaC)**:
   Terraform allows you to define cloud infrastructure in configuration files that can be versioned and reused.

2. **AWS EKS**:
   Amazon EKS simplifies Kubernetes management by handling control plane and scaling operations.

3. **Networking with VPC**:
   The Virtual Private Cloud (VPC) ensures secure and isolated networking for the EKS cluster.

4. **Terraform Modules**:
   Modular design promotes reusability. In this project, we used community modules for VPC and EKS setup.

---

## Step-by-Step Guide

### 1. Prerequisites
- **AWS CLI** installed and configured with appropriate credentials.
- **Terraform CLI** installed.
- **kubectl** installed for managing Kubernetes.
- **Git** installed for version control.

### 2. Clone the Repository
```bash
# Clone the demo project
$ git clone <repository-url>
$ cd <repository-folder>
```

### 3. Initialize Terraform
```bash
# Initialize the Terraform modules and providers
$ terraform init
```

### 4. Configure Variables
Edit the `terraform.tfvars` file to customize:
- `vpc_cidr_block`
- `private_subnet_cidr_blocks`
- `public_subnet_cidr_blocks`

Example `terraform.tfvars`:
```hcl
vpc_cidr_block = "10.0.0.0/16"
private_subnet_cidr_blocks = ["10.0.1.0/24", "10.0.2.0/24"]
public_subnet_cidr_blocks = ["10.0.3.0/24", "10.0.4.0/24"]
```

### 5. Apply the Configuration
```bash
# Deploy the infrastructure
$ terraform apply
```
Review the plan and type `yes` to confirm.

### 6. Update kubeconfig for Cluster Access
```bash
# Update your kubeconfig to connect to the cluster
$ aws eks update-kubeconfig --name myapp-eks-cluster --region eu-central-1
```

### 7. Verify Deployment
```bash
# Ensure kubectl is configured and working
$ kubectl get nodes
```

---

## Deploy Additional Resources
With the EKS cluster running, you can deploy resources such as:

### Example: Deploy Nginx
1. Create a deployment file `nginx-deployment.yaml`:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:latest
        ports:
        - containerPort: 80
```

2. Apply the deployment:
```bash
$ kubectl apply -f nginx-deployment.yaml
```

3. Expose the deployment as a LoadBalancer:
```bash
$ kubectl expose deployment nginx-deployment --type=LoadBalancer --port=80
```

---

## Best Practices

### Terraform Best Practices
- **State Management**: Use a remote backend (e.g., S3 with encryption) to manage Terraform state securely.
- **Modules**: Structure your Terraform code using reusable modules.
- **Versioning**: Lock provider versions to ensure consistent deployments.

### AWS & Kubernetes Security Best Practices
- **IAM Roles**: Grant least privilege access using IAM roles.
- **Encryption**: Enable encryption for sensitive data (e.g., secrets, storage).
- **Network Policies**: Define Kubernetes network policies to restrict pod communication.
- **Regular Updates**: Keep your Kubernetes version and Terraform modules up to date.

---

## Final Thoughts
By following this guide, you have automated the provisioning of an AWS EKS cluster and deployed resources efficiently. This approach highlights the power of Terraform in simplifying cloud infrastructure management.

Happy Deploying! 🚀
