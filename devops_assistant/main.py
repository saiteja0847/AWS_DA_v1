from agents.devops_agent import run_devops_agent
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Validate presence of required environment variables
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Missing OPENAI_API_KEY in environment. Please set it in your .env file.")
if not os.getenv("AWS_ACCESS_KEY_ID") or not os.getenv("AWS_SECRET_ACCESS_KEY"):
    raise ValueError("Missing AWS credentials. Please ensure AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are set in your .env file.")

def main():
    user_prompt = input("Enter your DevOps request: ")
    run_devops_agent(user_prompt)

if __name__ == "__main__":
    main()