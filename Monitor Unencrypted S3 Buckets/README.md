# Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

## Overview
This AWS Lambda function automatically detects any S3 buckets that do not have server-side encryption enabled. It uses **Boto3**, AWS’s Python SDK, to scan all buckets in the account and log the names of unencrypted buckets.

## Prerequisites
Before deploying and running the Lambda function, ensure you have:
- An **AWS account** with appropriate permissions
- Several **S3 buckets**, with at least one unencrypted
- **IAM Role with S3 read permissions** assigned to the Lambda function

## IAM Role Permissions
Create an IAM role with the following policy to allow the Lambda function to list all S3 buckets and retrieve their encryption status:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketEncryption"
            ],
            "Resource": "*"
        }
    ]
}
```

## Deployment Steps
### 1. Create an AWS Lambda Function
1. Navigate to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create function**.
3. Choose **Author from scratch**.
4. Enter a function name (e.g., `monitor-unencrypted-s3`).
5. Select **Python 3.x** as the runtime.
6. Assign the IAM role with S3 read access.
7. Click **Create function**.

### 2. Upload the Code
1. Upload the provided Python script (`lambda_function.py`) to the Lambda function.
2. Click **Deploy**.

### 3. Configure the Trigger (Optional)
1. Navigate to the **Triggers** section.
2. Click **Add trigger**.
3. Choose **EventBridge (CloudWatch Events)**.
4. Create a new rule to run the function periodically:
   - Rule type: **Schedule expression**
   - Expression: `rate(1 day)`
5. Click **Add**.

### 4. Test the Function
1. Click **Test** in the Lambda console.
2. Create a new test event with an empty JSON payload (`{}`).
3. Click **Invoke**.
4. Check the **CloudWatch Logs** to see detected unencrypted buckets.

## Screenshots
Below are screenshots demonstrating the setup and execution of the Lambda function:

### 1. AWS Lambda Function Setup
![Screenshot 2025-03-08 214407](https://github.com/user-attachments/assets/52aa8d06-d99d-4307-866c-b235970e511e)


### 2. IAM Role Permissions
![Screenshot 2025-03-08 205827](https://github.com/user-attachments/assets/48d34d0f-c9cc-4570-af52-c6bdaa9fd1d3)


### 3. Successful Testing
![Screenshot 2025-03-08 212951](https://github.com/user-attachments/assets/bf3e576b-168c-4e73-90bf-b6734cfee7de)


## Expected Output
If unencrypted buckets exist, the response will look like:
```json
{
    "Unencrypted Buckets": ["bucket1", "bucket2"]
}
```
If all buckets are encrypted, the response will be:
```json
{
    "Unencrypted Buckets": "All buckets are encrypted"
}
```

## Conclusion
This Lambda function provides an automated way to monitor the encryption status of S3 buckets and ensure compliance with security best practices. You can modify the function to send notifications when unencrypted buckets are detected.

---

### **Next Steps**
✅ Modify the function to send **SNS notifications** when unencrypted buckets are found.  
✅ Schedule the function to run at **custom intervals** using EventBridge.  
✅ Extend functionality to **automatically enable encryption** for unencrypted buckets.  

---

### **Author:** Reshma Navale  
📅 **Date:** March 2025


