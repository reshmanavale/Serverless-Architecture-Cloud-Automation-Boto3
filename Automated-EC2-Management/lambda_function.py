import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Fetch all instances
    response = ec2.describe_instances(Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop', 'Auto-Start']}])

    instances_to_stop = []
    instances_to_start = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'] == 'Action' and tag['Value'] == 'Auto-Stop':
                    instances_to_stop.append(instance['InstanceId'])
                elif tag['Key'] == 'Action' and tag['Value'] == 'Auto-Start':
                    instances_to_start.append(instance['InstanceId'])

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
