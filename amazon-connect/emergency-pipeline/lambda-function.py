import boto3
import json

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='eu-central-1')

    # Define the EC2 instance parameters
    instance_params = {
        'ImageId': 'ami-0abcdef1234567890',  # Replace with a valid AMI ID
        'InstanceType': 't2.micro',         # Replace with desired instance type
        'MinCount': 1,
        'MaxCount': 1,
        'KeyName': 'your-key-pair-name',    # Replace with your key pair name
        'SecurityGroupIds': ['sg-0abc1234def567890'],  # Replace with your security group ID
        'SubnetId': 'subnet-0abc1234def567890'         # Replace with your subnet ID
    }

    try:
        # Create the EC2 instance
        response = ec2_client.run_instances(**instance_params)
        instance_id = response['Instances'][0]['InstanceId']

        return {
            'statusCode': 200,
            'body': json.dumps(f"EC2 instance {instance_id} created successfully.")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error creating EC2 instance: {str(e)}")
        }
