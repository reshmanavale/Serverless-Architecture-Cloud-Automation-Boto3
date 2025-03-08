# Serverless Architecture Cloud Automation Using AWS Lambda & Boto3

## Overview
This repository contains AWS Lambda functions that automate various AWS cloud tasks using **Boto3**, the AWS SDK for Python. Each folder represents a different automation use case, making cloud operations more efficient and cost-effective.

## Repository Structure

### 1️⃣ **Automated EC2 Management**
📌 **Objective:** Automate EC2 instance management using AWS Lambda and Boto3.  
✅ Start, stop, and monitor EC2 instances.  
✅ Schedule automation using AWS CloudWatch Events.  
📂 Folder: `Automated-EC2-Management`

### 2️⃣ **Automated S3 Bucket Cleanup**
📌 **Objective:** Automatically delete old files from an S3 bucket.  
✅ Delete files older than **5 minutes** (configurable).  
✅ Uses **AWS Lambda & Boto3** to interact with S3.  
📂 Folder: `Automated S3 Bucket Cleanup`

### 3️⃣ **Monitor Unencrypted S3 Buckets**
📌 **Objective:** Detect S3 buckets without **server-side encryption** enabled.  
✅ Scan all S3 buckets in the AWS account.  
✅ Log unencrypted bucket names for security monitoring.  
📂 Folder: `Monitor Unencrypted S3 Buckets`

### 4️⃣ **Auto-Tagging EC2 Instances**
📌 **Objective:** Automatically tag newly launched EC2 instances.  
✅ Assigns tags like **launch date** and **custom tags**.  
✅ Triggered via **AWS CloudWatch Events** when an EC2 instance starts.  
📂 Folder: `Auto-Tagging EC2 Instances`

## How to Use
1. Clone this repository:  
   ```sh
   git clone https://github.com/reshmanavale/Serverless-Architecture-Cloud-Automation-Boto3.git
   cd Serverless-Architecture-Cloud-Automation-Boto3
