# Automated S3 Bucket Cleanup Using AWS Lambda and Boto3

## Overview
This AWS Lambda function automatically deletes files older than **30 days** from a specified S3 bucket. It uses **Boto3**, AWS’s Python SDK, to interact with S3 and remove outdated objects.

## Prerequisites
Before deploying and running the Lambda function, ensure you have:
- An **AWS account** with appropriate permissions
- An **S3 bucket** containing test files
- AWS CLI or AWS Management Console access
- **IAM Role with S3 permissions** assigned to the Lambda function

## IAM Role Permissions
Create an IAM role with the following policy to allow the Lambda function to list and delete objects in the S3 bucket:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}
```

Replace `your-bucket-name` with the actual S3 bucket name.

## Deployment Steps
### 1. Create an AWS Lambda Function
1. Navigate to the [AWS Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create function**.
3. Choose **Author from scratch**.
4. Enter a function name (e.g., `s3-cleanup-lambda`).
5. Select **Python 3.x** as the runtime.
6. Assign the IAM role with S3 access.
7. Click **Create function**.

### 2. Upload the Code
1. Upload the provided Python script (`lambda_function.py`) to the Lambda function.
2. Click **Deploy**.

### 3. Configure the Trigger
1. Navigate to the **Triggers** section.
2. Click **Add trigger**.
3. Choose **EventBridge (CloudWatch Events)**.
4. Create a new rule to run the function every 5 minutes:
   - Rule type: **Schedule expression**
   - Expression: `rate(30 days)`
5. Click **Add**.

### 4. Test the Function
1. Click **Test** in the Lambda console.
2. Create a new test event with a sample payload (empty JSON `{}` is fine).
3. Click **Invoke**.
4. Check the **CloudWatch Logs** to see deleted files.

## Screenshots
Below are screenshots demonstrating the setup and execution of the Lambda function:

### 1. AWS Lambda Function Setup
![Lambda Setup](screenshots/lambda_setup.png)

### 2. IAM Role Permissions
![IAM Role](screenshots/iam_role.png)

### 3. Adding EventBridge Trigger
![EventBridge Trigger](screenshots/eventbridge_trigger.png)

### 4. CloudWatch Logs Showing Deleted Files
![CloudWatch Logs](screenshots/cloudwatch_logs.png)

## Expected Output
If files older than **30 days** exist, the response will look like:
```json
{
    "Deleted Files": ["file1.txt", "file2.log"]
}
```
If no files meet the criteria, the response will be:
```json
{
    "Deleted Files": "No files deleted"
}
```

## Conclusion
This Lambda function provides an automated way to clean up old files from an S3 bucket. You can modify the retention period by changing `minutes=5` to `days=30` or any other value as needed.

---

### 📌 **Next Steps**
✅ Modify the function to work with **different time periods**.
✅ Schedule the function to run at **custom intervals** using EventBridge.
✅ Extend functionality to **exclude specific file types or prefixes**.

---

### **Author:** Reshma Navale
📅 **Date:** March 2025

