


import boto3

def start_instance(instance_id: str, region_name: str = "us-east-1") -> str:
    ec2 = boto3.client("ec2", region_name=region_name)
    ec2.start_instances(InstanceIds=[instance_id])
    return f"Started instance {instance_id}"

def stop_instance(instance_id: str, region_name: str = "us-east-1") -> str:
    ec2 = boto3.client("ec2", region_name=region_name)
    ec2.stop_instances(InstanceIds=[instance_id])
    return f"Stopped instance {instance_id}"

def reboot_instance(instance_id: str, region_name: str = "us-east-1") -> str:
    ec2 = boto3.client("ec2", region_name=region_name)
    ec2.reboot_instances(InstanceIds=[instance_id])
    return f"Rebooted instance {instance_id}"

def terminate_instance(instance_id: str, region_name: str = "us-east-1") -> str:
    ec2 = boto3.client("ec2", region_name=region_name)
    ec2.terminate_instances(InstanceIds=[instance_id])
    return f"Terminated instance {instance_id}"