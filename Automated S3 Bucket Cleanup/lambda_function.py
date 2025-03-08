import boto3
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize S3 client
s3 = boto3.client("s3")

# Define bucket name
BUCKET_NAME = "reshma-bucket-cleanup-123"

# Set a cutoff time for 30 days
cutoff_date = datetime.datetime.utcnow() - datetime.timedelta(days=30)

def lambda_handler(event, context):
    deleted_files = []

    try:
        # List all objects in the bucket
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

        if "Contents" in response:
            for obj in response["Contents"]:
                file_name = obj["Key"]
                last_modified = obj["LastModified"]

                # Convert last_modified to UTC without timezone info
                if last_modified.replace(tzinfo=None) < cutoff_date:
                    # File is older than 5 minutes, delete it
                    s3.delete_object(Bucket=BUCKET_NAME, Key=file_name)
                    deleted_files.append(file_name)
                    logger.info(f"Deleted: {file_name} (Last Modified: {last_modified})")

    except Exception as e:
        logger.error(f"Error processing S3 bucket: {str(e)}")

    return {
        "Deleted Files": deleted_files if deleted_files else "No files deleted"
    }

