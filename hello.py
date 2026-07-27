import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-0abcdef1234567890',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

print("EC2 instance created:", instance[0].id)