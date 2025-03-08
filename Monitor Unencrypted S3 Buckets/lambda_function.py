import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    # Get a list of all S3 buckets
    response = s3.list_buckets()

    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        
        # Get the bucket encryption status
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        except s3.exceptions.ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                # Bucket does not have server-side encryption
                unencrypted_buckets.append(bucket_name)
    
    # Logging output
    if unencrypted_buckets:
        print(f"Unencrypted S3 Buckets: {unencrypted_buckets}")
    else:
        print("All buckets have encryption enabled.")

    return {
        "UnencryptedBuckets": unencrypted_buckets if unencrypted_buckets else "All buckets are encrypted"
    }
