import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='SG from boto3',
    GroupName='boto3-security-group',
    VpcId='vpc-06c068119b33ff027',
)

print(response["GroupId"])