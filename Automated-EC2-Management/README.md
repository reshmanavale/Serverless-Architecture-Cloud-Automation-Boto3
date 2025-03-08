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
- [ ] ![Screenshot 2025-03-05 082554](https://github.com/user-attachments/assets/26893f7f-b35d-413d-b90c-983bc1f24d7d)

- [ ] IAM role creation
- [ ] ![Screenshot 2025-03-08 183003](https://github.com/user-attachments/assets/c796cab6-7732-4011-a027-ebda34eb0173)

- [ ] Lambda function configuration
      ![Screenshot 2025-03-05 083320](https://github.com/user-attachments/assets/caa479e9-2a11-45d8-bada-f68c682f201d)

- [ ] Successful Testing
      ![Screenshot 2025-03-05 083212](https://github.com/user-attachments/assets/893069cb-b4ef-422c-bf68-a546150c3016)


