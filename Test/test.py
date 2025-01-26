from dotenv import load_dotenv
from mira_sdk import MiraClient
import os

load_dotenv()
client = MiraClient(config={"API_KEY": os.getenv("MIRA_API_KEY")})
print("Client created successfully")
