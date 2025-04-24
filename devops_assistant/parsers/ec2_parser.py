from dotenv import load_dotenv
import os
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from pathlib import Path

load_dotenv()  # Explicitly load .env file into environment

# Load schema
with open("docs/ec2_schema.json") as f:
    SCHEMA = json.load(f)

llm = ChatOpenAI(temperature=0, model="gpt-4")

def extract_parameters_from_prompt(prompt: str) -> dict:
    param_names = list(SCHEMA.keys())

    system_prompt = f"""
You are an assistant that extracts EC2 instance creation parameters from text prompts.
Valid parameter names are: {', '.join(param_names)}.
Return a JSON object where the keys are only from the above list, and values are inferred from the user prompt.
DO NOT guess values that are not mentioned.
Example: 'Create t2.micro EC2 named devbox in us-west-2' → {{
  "InstanceType": "t2.micro",
  "TagSpecifications": [{{"ResourceType": "instance", "Tags": [{{"Key": "Name", "Value": "devbox"}}]}}],
  "Placement": {{"AvailabilityZone": "us-west-2a"}}
}}
""".strip()

    full_prompt = PromptTemplate.from_template("{prompt}").format(prompt=prompt)
    response = llm.invoke(system_prompt + "\n\nUser Prompt:\n" + prompt)

    try:
        extracted = json.loads(response.content)
    except Exception:
        extracted = {}

    return extracted