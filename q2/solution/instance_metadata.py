import boto3
import json
import sys

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Retrieve instance metadata
response = ec2_client.describe_instances()
instance_data = response['Reservations'][0]['Instances'][0]

# Extract relevant metadata
instance_id = instance_data['InstanceId']
public_ip = instance_data.get('PublicIpAddress', '')
private_ip = instance_data['PrivateIpAddress']
availability_zone = instance_data['Placement']['AvailabilityZone']
instance_type = instance_data['InstanceType']

# Create a dictionary with the metadata
metadata = {
    'instance_id': instance_id,
    'public_ip': public_ip,
    'private_ip': private_ip,
    'availability_zone': availability_zone,
    'instance_type': instance_type
}

# Convert the dictionary to JSON
metadata_json = json.dumps(metadata, indent=2)

# Print the JSON output
print(metadata_json)

# Function to retrieve a specific metadata value
def get_metadata(key):
    if key in metadata:
        return metadata[key]
    else:
        return None

# Check if a specific key was provided as a command-line argument
if len(sys.argv) == 2:
    key = sys.argv[1]
    value = get_metadata(key)

    if value is not None:
        print(f'{key}: {value}')
    else:
        print(f'Key "{key}" not found in instance metadata.')
else:
    print('Usage: python get_instance_metadata.py <metadata_key>')
