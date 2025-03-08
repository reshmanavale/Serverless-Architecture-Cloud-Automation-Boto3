import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    print("Fetching EC2 instances with Auto-Stop and Auto-Start tags...")
    
    try:
        response = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop', 'Auto-Start']}])

        instances_to_stop = []
        instances_to_start = []
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                for tag in instance.get('Tags', []):
                    if tag['Key'] == 'Action':
                        if tag['Value'] == 'Auto-Stop':
                            instances_to_stop.append(instance_id)
                        elif tag['Value'] == 'Auto-Start':
                            instances_to_start.append(instance_id)

        print(f"Instances to Stop: {instances_to_stop}")
        print(f"Instances to Start: {instances_to_start}")

        # Stop instances
        if instances_to_stop:
            ec2.stop_instances(InstanceIds=instances_to_stop)
            print(f"Stopped instances: {instances_to_stop}")

        # Start instances
        if instances_to_start:
            ec2.start_instances(InstanceIds=instances_to_start)
            print(f"Started instances: {instances_to_start}")

        return {
            'statusCode': 200,
            'body': f"Stopped instances: {instances_to_stop}, Started instances: {instances_to_start}"
        }
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
