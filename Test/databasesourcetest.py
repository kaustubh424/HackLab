from mira_sdk import MiraClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("MIRA_API_KEY")

# Initialize the client
client = MiraClient(config={"API_KEY": api_key})

# Create dataset
client.dataset.create("khushalsarode/hackathon-description", "A dataset for storing hackathon descriptions.")
print("Dataset created successfully.")
# Add URL to your data set (URL must be added to an existing dataset)
#client.dataset.add_source("venmus/mira-whitepaper", url="https://mira.network/")

# Add file to your data set (file must be added to an existing dataset)
#client.dataset.add_source("venmus/mira-whitepaper", file_path="mira-whitepaper.pdf")