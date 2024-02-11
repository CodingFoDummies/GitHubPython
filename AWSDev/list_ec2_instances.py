#Import all libraries and modules
import boto3

#open management console

aws_management_console = boto3.Session(profile_name="default",region_name='us-east-2')


#open EC2 console

ec2_console = aws_management_console.client(service_name='ec2')
result= ec2_console.describe_instances()['Reservations']
print(result)


# response = ec2_instance.run_instances(
#         ImageId = 'ami-0c20d88b0021158c6',
#         InstanceType = 't2.micro',
#         MaxCount = 1,
#         MinCount =1
# )
