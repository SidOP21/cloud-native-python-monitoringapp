import boto3

ecr_client = boto3.client('ecr', region_name= 'ap-south-1')

repository_name = "my-cloud-native-repo-py"

response = ecr_client.create_repository(repositoryName= repository_name)

repository_uri = response['repository']['repositoryUri']

print(repository_uri)