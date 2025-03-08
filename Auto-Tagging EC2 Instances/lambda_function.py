import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
import boto3
import datetime

def lambda_handler(event, context):
    ec2_client = boto3.client("ec2")
    
    # Extract instance ID from the event
    detail = event.get("detail", {})
    instance_id = detail.get("instance-id")
    
    if not instance_id:
        print("No instance ID found in the event.")
        return
    
    # Generate current date tag
    current_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    
    # Define tags to apply
    tags = [
        {"Key": "LaunchDate", "Value": current_date},
        {"Key": "Environment", "Value": "Auto-Tagged"}
    ]
    
    try:
        # Apply tags to the instance
        ec2_client.create_tags(Resources=[instance_id], Tags=tags)
        print(f"Successfully tagged instance {instance_id} with {tags}")
    except Exception as e:
        print(f"Error tagging instance {instance_id}: {str(e)}")
