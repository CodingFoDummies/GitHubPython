import boto3

class EC2Class:
    region = 'us-east-2'
    service_name = 'ec2'
    instance_type = 't2.micro'
    ImageId = 'ami-0c20d88b0021158c6'
    min_count = 1
    max_count = 1

   
    def __init__(self, region, service_name, machine_type, ImageId):
        self.region = region
        self.service_name = service_name
        self.machine_type = machine_type
        self.ImageId = ImageId


    def create_ec2_instances()->None:
        try:
            ec2_resource = boto3.client('ec2')
            print("creating EC2 instances")
            
            result = ec2_resource.run_instances(
                ImageId = 'ami-0c20d88b0021158c6',
                min_count = 1,
                max_count = 1,
                instance_type = 't2.micro'
                )
            return result
        except Exception as e:
            print(e)
    


 

Ec1 = EC2Class('us-west-1', 'ec2', 't2.micro', 'ami-0c20d88b0021158c6')

# Ec22 = EC2Class('us-west-22', 'ec22', 't3.micro', '222234444')

# print("Ec1 details")
# print('ec1 region is ', Ec1.region)


# print("Ec22 details")
# print('ec22 region is ', Ec22.region)
# #global

# print("global region is ", EC2Class.region)

#creating an instance
result = Ec1.create_ec2_instances()


#ec2_instance = boto3.client(service_name='ec2', region_name='us-east-2')



# response = ec2_instance.terminate_instances(
#     InstanceIds=[
#         'i-0cbb187254403f09c'
#     ]
# )

# print(response)