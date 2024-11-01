# main.tf
provider "aws" {
  region = "af-south-1"  # e.g., us-west-2
}

# IAM Role for EC2 to access ECR
resource "aws_iam_role" "ec2_role" {
  name = "ec2-ecr-role"
  assume_role_policy = jsonencode({
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  })
}

# Attach ECR Read-Only policy to the role
resource "aws_iam_policy_attachment" "ecr_access" {
  name       = "ecr-access-policy-attachment"
  roles      = [aws_iam_role.ec2_role.name]
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

# Instance Profile to attach IAM Role to EC2
resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = "ec2-ecr-instance-profile"
  role = aws_iam_role.ec2_role.name
}

variable "user_data_script" {
  default = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y docker
    service docker start
    usermod -aG docker ec2-user

    # Login to ECR
    aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.your-region.amazonaws.com

    # Pull the Docker image and run it
    docker pull your-account-id.dkr.ecr.your-region.amazonaws.com/your-repo-name:tag
    docker run -d --name your-container-name your-account-id.dkr.ecr.your-region.amazonaws.com/your-repo-name:tag
  EOF
}
resource "aws_instance" "ec2_instance" {
  ami           = "ami-0f648cb3af764749a"  # Replace with your desired AMI ID, e.g., Amazon Linux 2 AMI
  instance_type = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.ec2_instance_profile.name
  user_data           = var.user_data_script

  # Optionally, specify security groups, key pair, etc.
  key_name      = "Django_tcgc_cms"  # Ensure you've created this key pair in your AWS region

  tags = {
    Name = "ECR-EC2-Instance"
  }
}
