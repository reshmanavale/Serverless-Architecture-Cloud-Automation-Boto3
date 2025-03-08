# Automated EC2 Instance Management Using AWS Lambda and Boto3

## Objective
Automate the stopping and starting of EC2 instances based on their tags using AWS Lambda and Boto3.

## Steps

### 1. EC2 Setup
- Created two EC2 instances (`t2.micro`).
- Tagged one with **Action=Auto-Stop**.
- Tagged the other with **Action=Auto-Start**.

### 2. IAM Role for Lambda
- Created an IAM role (`LambdaEC2ManagerRole`) with `AmazonEC2FullAccess`.

### 3. Lambda Function
- Created a Lambda function (`EC2AutoManager`) with Python 3.x.
- Assigned the IAM role.
- Wrote the Python script using Boto3 to stop/start EC2 instances.

### 4. Testing
- Manually invoked the function.
- Verified that:
  - `Auto-Stop` instances stopped.
  - `Auto-Start` instances started.

### 5. Screenshots
- [ ] EC2 instance setup
- [ ] IAM role creation
- [ ] Lambda function configuration
- [ ] CloudWatch logs

