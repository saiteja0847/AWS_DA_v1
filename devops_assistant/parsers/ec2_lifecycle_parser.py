import re

def parse_ec2_lifecycle_prompt(prompt: str) -> dict:
    """
    Extract action and instance ID from prompt.
    Expected to find words like 'start', 'stop', 'terminate', 'reboot' and an instance ID like 'i-1234567890abcdef0'
    """
    actions = ["start", "stop", "terminate", "reboot"]
    action = None

    for a in actions:
        if a in prompt.lower():
            action = a
            break

    instance_id_match = re.search(r"(i-[a-z0-9]{8,})", prompt)
    instance_id = instance_id_match.group(1) if instance_id_match else None

    return {
        "action": action,
        "instance_id": instance_id
    }
