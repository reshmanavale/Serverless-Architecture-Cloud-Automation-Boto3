# Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## Overview
This AWS Lambda function automatically assigns tags to newly launched EC2 instances. The function ensures proper resource tracking by adding a tag with the **current date** and a custom tag (e.g., `Environment: Auto-Tagged`).

## Prerequisites
Before deploying the Lambda function, ensure you have:
- An **AWS account** with access to EC2 and Lambda
- IAM role with the required permissions
- EC2 instances for testing

## IAM Role Permissions
Create an IAM role with the following policy to allow the Lambda function to tag EC2 instances:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*"
        }
    ]
}
```

## Deployment Steps

### 1. Create an AWS Lambda Function
1. Navigate to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create function**.
3. Choose **Author from scratch**.
4. Enter a function name (e.g., `AutoTagEC2Instance`).
5. Select **Python 3.x** as the runtime.
6. Assign the IAM role created in the previous step.
7. Click **Create function**.

### 2. Upload the Code
1. Upload the provided Python script (`lambda_function.py`) to the Lambda function.
2. Click **Deploy**.

### 3. Configure CloudWatch Event Trigger
1. Navigate to the **Triggers** section.
2. Click **Add trigger**.
3. Choose **EventBridge (CloudWatch Events)**.
4. Create a new rule to capture EC2 instance launch events:
   - **Event source**: AWS API Call via CloudTrail
   - **Event type**: EC2 Instance State-change Notification
   - **Detail type**: EC2 Instance Launch
5. Click **Add**.

### 4. Manual Testing
1. **Get an existing EC2 Instance ID**:
   - Go to the **EC2 Console** → Click **Instances**.
   - Select a running instance and copy its **Instance ID**.
2. **Create a test event in Lambda**:
   - Go to **Lambda Console** → Click on your function.
   - Click the **Test** tab → **Create new test event**.
   - Use the following JSON:

```json
{
  "detail": {
    "instance-id": "i-0abcd1234efgh5678",
    "state": "running"
  }
}
```
> **Replace** `i-0abcd1234efgh5678` with an actual instance ID.

3. Click **Test** to invoke the function.
4. Go to **EC2 Console** → **Instances** → **Tags** tab to verify tagging.

## Screenshots
Below are screenshots demonstrating the setup and execution of the Lambda function:

### 1. AWS Lambda Function Setup
<img width="932" alt="image" src="https://github.com/user-attachments/assets/8a43ab7c-2f52-4391-9719-0cc81d9b76d0" />

### 2. IAM Role Permissions
<img width="950" alt="image" src="https://github.com/user-attachments/assets/09b35d69-44bb-4cfb-9df9-9fdd75eb3a11" />

### 4. EC2 Instance Tags After Execution
![Screenshot 2025-03-08 230026](https://github.com/user-attachments/assets/e558c7d5-7036-4289-806c-61a2c08d2fc3)
![Screenshot 2025-03-08 230109](https://github.com/user-attachments/assets/ac9d5417-eb07-4528-a6bd-fa56e48960b0)


## Expected Output
If successful, the function will tag instances with:
- `LaunchDate`: Current date (`YYYY-MM-DD`)
- `Environment`: `Auto-Tagged`

```json
{
    "Instance ID": "i-0abcd1234efgh5678",
    "Status": "Successfully tagged"
}
```

## Conclusion
This Lambda function automates EC2 instance tagging, ensuring better organization and tracking. You can extend the functionality to tag instances based on custom rules.

---

### 📌 **Next Steps**
✅ Modify the function to apply **different tags** based on instance type or region.
✅ Schedule the function to run at **custom intervals**.
✅ Extend functionality to **tag instances based on owner, department, or cost center**.

---

### **Author:** Reshma Navale 
📅 **Date:** March 2025


