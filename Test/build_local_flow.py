from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})
print("Client initialized")
flow = Flow(source="project-idea-generation-flow.yaml")
print("Flow initialized")
input_dict = {
    "industry": "Healthcare",
    "technology_preference": "AI",
    "prize_sponsors": "Google Cloud",
    "project_scale": "Team",
    "objective": "Problem-solving",
    "deadline": "2 days",
}
print("Input dictionary initialized")
# industry_type project_name primary_keywords secondary_keywords extensions
response = client.flow.test(flow, input_dict)
print("Response received")  
print(response)
