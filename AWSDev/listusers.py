import boto3

aws_management_console = boto3.Session(profile_name="default")
iam_console = aws_management_console.resource('iam')

for each_user in iam_console.users.all():
    print(each_user.name)

aws_management_console = boto3.Session(profile_name='default')
iam_console_client = aws_management_console.client('iam')

for each_user in iam_console_client.list_users()['Users']:
    print(each_user['UserName'])

    




