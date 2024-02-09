import boto3

ec2_instance = boto3.client(service_name='ec2', region_name='us-east-2')



response = ec2_instance.terminate_instances(
    InstanceIds=[
        'i-0cbb187254403f09c'
    ]
)

print(response)