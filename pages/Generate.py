import streamlit as st
from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize MiraClient
api_key = os.getenv("MIRA_API_KEY")
client = MiraClient(config={"API_KEY": api_key})

# Streamlit layout configuration
st.set_page_config(page_title="Domain Name Generator", layout="wide")

# Title and intro section
st.title("🌐 Domain Name & SEO Metadata Generator")
st.write(
    """
    Welcome to the **Domain Name and SEO Metadata Generator**! 🚀
    This tool helps you generate creative domain names, SEO-friendly metadata, and taglines for your projects, perfect for hackathons, startups, and more.
    """
)

# Input fields with styling and placeholders
industry_type = st.text_input("🏭 Industry Type", "IT productivity tool")
project_name = st.text_input("📁 Project Name", "genaidomains")
project_description = st.text_area("📝 Project Description", "A tool to generate domain names and SEO metadata.")
primary_keywords = st.text_input("🔑 Primary Keywords", "genaidomain metatags seogenerator")
secondary_keywords = st.text_input("📝 Secondary Keywords", "domainnameideas projecttaglines")
extensions = st.text_input("🌍 Extensions (comma-separated)", ".com, .co, .io")

# Action button for generating results
st.write("---")
if st.button("🔄 Generate Domain Names & Metadata"):
    with st.spinner("Generating domain names and metadata... 🔧"):
        try:
            # Set up the flow and input parameters
            flow = Flow(source="./flows/generate-domain-names-for-projects.yaml")
            input_dict = {
                "industry_type": industry_type,
                "project_name": project_name,
                "project_description": project_description,
                "primary_keywords": primary_keywords,
                "secondary_keywords": secondary_keywords,
                "extensions": extensions.replace(" ", "").split(","),
            }
            
            # Get results from Mira SDK
            response = client.flow.test(flow, input_dict)
            result = response.get("result", "No results found. 😞")
            
            # Display results
            st.subheader("🎉 Generated Domain Names & SEO Metadata")
            st.markdown(f"**Domain Names:** {result['domain_names']}")
            st.markdown(f"**SEO Metadata:** {result['seo_metadata']}")
            st.markdown(f"**Taglines:** {result['taglines']}")

        except Exception as e:
            st.error(f"❌ An error occurred: {e}")
