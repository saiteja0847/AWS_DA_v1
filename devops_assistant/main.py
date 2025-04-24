from agents.devops_agent import run_devops_agent
from dotenv import load_dotenv
import os
from agents.ec2_lifecycle_agent import run_ec2_lifecycle_agent
from parsers.ec2_lifecycle_parser import parse_ec2_lifecycle_prompt

# Load environment variables from .env
load_dotenv()

# Validate presence of required environment variables
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Missing OPENAI_API_KEY in environment. Please set it in your .env file.")
if not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"):
    raise ValueError("Missing AWS credentials. Please ensure AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set in your .env file.")

def main():
    user_prompt = input("Enter your DevOps request: ").strip()

    # First try lifecycle parsing
    parsed_life = parse_ec2_lifecycle_prompt(user_prompt)
    action = parsed_life.get("action")
    instance_id = parsed_life.get("instance_id")

    if action and instance_id:
        result = run_ec2_lifecycle_agent(action, instance_id, region_name="us-east-1")
        print(result)
    else:
        # Fall back to EC2 create flow
        run_devops_agent(user_prompt)

if __name__ == "__main__":
    main()