from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

version = "version_1" # Specify the version of the flow to use
input_data = {"imput": "data"} # Input data for the flow

# If no version is provided it'll use latest version by default
if version:
	flow_name = f"khushalsarode/flowname/{version}"
else:
	flow_name = "khushalsarod/flowname"

result = client.flow.execute(flow_name, input_data)
print(result)