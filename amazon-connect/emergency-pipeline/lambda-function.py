import boto3
import json

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='eu-central-1')  # Replace with your region

    # Define the EC2 instance parameters
    instance_params = {
        'ImageId': 'ami-015cbce10f839bd0c',
        'InstanceType': 't2.micro',
        'MinCount': 1,
        'MaxCount': 1,
        'KeyName': 'emergency-pipeline-ec2',
        'SecurityGroupIds': ['sg-06ab1cf2182ba8e88'],
        'SubnetId': 'subnet-123456d2dc11c5bba'
    }
    
    try:
        # Create the EC2 instance
        response = ec2_client.run_instances(**instance_params)
        instance_id = response['Instances'][0]['InstanceId']

        # Return the instance ID immediately
        return {
            'statusCode': 200,
            'body': instance_id
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Error creating EC2 instance',
                'details': str(e)
            })
        }
