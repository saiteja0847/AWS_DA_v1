import boto3
import json

def create_ec2_instance(**kwargs):
    region_name = kwargs.get("Placement", {}).get("AvailabilityZone", "")[:-1]  # Strip 'a' from 'us-west-2a'
    if not region_name:
        region_name = kwargs.get("region_name", "us-east-1")

    print(f"[DEBUG] Using region: {region_name}")
    print(f"[DEBUG] EC2 create_instances parameters:\n{json.dumps(kwargs, indent=2)}")

    confirmation = input("Proceed with these parameters? (yes/no): ").strip().lower()
    if confirmation != "yes":
        return "EC2 instance launch aborted by user."

    ec2 = boto3.resource("ec2", region_name=region_name)

    try:
        instances = ec2.create_instances(**kwargs)
        return f"EC2 instance launched with ID: {instances[0].id}"
    except Exception as e:
        return f"Failed to launch EC2 instance: {str(e)}"
