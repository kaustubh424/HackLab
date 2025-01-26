import streamlit as st
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize MiraClient
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

# Streamlit app title and description
st.set_page_config(page_title="Hackathon Description Summarizer", layout="wide")
st.title("💡 Hackathon Description Summarizer")

st.write(
    """
    Welcome to the **Hackathon Description Summarizer**! 🚀
    Simply paste your hackathon description below, and we'll generate a summarized view including:
    
    - **Key details** about the hackathon
    - **Prize information**
    - **Guidelines and tips** to help you get started!
    """
)

# Hackathon description input
hackathon_description = st.text_area(
    "🔍 Paste Hackathon Description Here", 
    "Paste your hackathon description here to get a summarized view of the event. 📝"
)

# Action button for generating results
st.write("---")
if st.button("⚡ Generate Summary"):
    with st.spinner("Generating summary... 🔧"):
        try:
            # Run the flow to generate a summary
            flow = Flow(source="./flows/hackathon-summary-rag.yaml")
            input_dict = {"hackathon_description": hackathon_description}
            response = client.flow.test(flow, input_dict)
            result = response.get("result", "No results found. 😞")

            # Display results
            st.subheader("✨ Hackathon Description Summary")
            if result:
                st.markdown(result)
            else:
                st.write("No relevant information found. Please check the description.")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

