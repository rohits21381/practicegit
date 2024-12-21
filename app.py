import boto3

def lambda_handler(event, context):
    """
    Function to start an EC2 instance.
    """
    ec2 = boto3.client('ec2')
    
    # Replace with your instance ID
    instance_id = 'i-0abcd1234efgh5678'
    
    # Start the instance
    ec2.start_instances(InstanceIds=[instance_id])
    
    print(f"Started EC2 instance: {instance_id}")
    
    return {
        'statusCode': 200,
        'body': f"EC2 instance {instance_id} started successfully."
    }

