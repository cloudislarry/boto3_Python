import boto3

s3 = boto3.client('s3')

response = s3.create_bucket (
    Bucket='ljohns-boto-05162023'
    )
    
print(response)