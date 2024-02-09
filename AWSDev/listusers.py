#Import all modules and libraries
import boto3

#open management console
aws_management_console = boto3.Session(profile_name="default")

#user resource method to get access to IAM
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)

#Use client method to get access to iam users
iam_console_client = aws_management_console.client('iam')

for each_user in iam_console_client.list_users()['Users']:
    print(each_user['UserName'])

# Create User
# iam_console_client.create_user (UserName='narendra-test')
    
# #delete user
# user_name = "narendra-test"
# iam_console_client.delete_user(UserName = user_name)
# print(user_name + " user deleted")




