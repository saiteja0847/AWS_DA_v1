

from langchain.agents import Tool
from langchain_community.chat_models import ChatOpenAI
from tools.ec2_tools import create_ec2_instance
from parsers.ec2_parser import extract_parameters_from_prompt
import json

llm = ChatOpenAI(temperature=0)

def run_devops_agent(prompt: str):
    # Extract parameters from prompt using LLM + schema
    extracted_params = extract_parameters_from_prompt(prompt)

    print("[DEBUG] Extracted parameters:")
    print(json.dumps(extracted_params, indent=2))

    # Ensure mandatory params are filled in
    required = ["ImageId", "MinCount", "MaxCount"]
    for key in required:
        if key not in extracted_params:
            extracted_params[key] = input(f"Enter value for required field '{key}': ")

    # Convert MinCount and MaxCount to int
    extracted_params["MinCount"] = int(extracted_params["MinCount"])
    extracted_params["MaxCount"] = int(extracted_params["MaxCount"])

    # Call boto3 EC2 creator
    result = create_ec2_instance(**extracted_params)
    print(result)