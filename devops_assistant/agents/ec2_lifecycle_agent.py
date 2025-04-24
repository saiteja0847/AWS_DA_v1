


from tools.ec2_lifecycle import (
    start_instance,
    stop_instance,
    reboot_instance,
    terminate_instance
)

def run_ec2_lifecycle_agent(action: str, instance_id: str, region_name: str = "us-east-1") -> str:
    try:
        if action == "start":
            return start_instance(instance_id, region_name)
        elif action == "stop":
            return stop_instance(instance_id, region_name)
        elif action == "reboot":
            return reboot_instance(instance_id, region_name)
        elif action == "terminate":
            return terminate_instance(instance_id, region_name)
        else:
            return f"Unsupported action: {action}"
    except Exception as e:
        return f"Error executing {action} on instance {instance_id}: {str(e)}"