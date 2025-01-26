import streamlit as st

# Set page configuration
st.set_page_config(page_title="About the App", layout="wide")

# Title of the section
st.title("💡 About the App")

# What is this app?
st.write("### 🤖 What is this app?")
st.write(
    """
    This app provides various tools designed for **hackathon participants** and **project creators** to make their journey smoother and more efficient:

    - 🌐 **Domain Name Generator**: Create optimized **domains**, **SEO metadata**, and **taglines** for your projects to enhance your online presence.
    - 🏅 **Hackathon Summarizer**: Summarizes hackathon details, prize information, guidelines, and gives tips for better preparation.
    - 💡 **Project Idea Generator**: Generates **suitable project ideas** based on hackathon details or your project's goals, technology stack, and more.
    """
)

# How it works
st.write("### 🛠️ How it Works")
st.write(
    """
    - 🌟 **Generate Domains**: Provide your industry type, project name, and keywords to generate optimized domains, SEO tags, and taglines.
    - 📜 **Summarize Hackathons**: Get a summarized description of hackathons, prize details, guidelines, and tips for your next hackathon.
    - 🚀 **Generate Project Ideas**: Input hackathon details and project goals to receive project ideas with suggested tech stacks and outcomes.
    """
)

# Tech Stack
st.write("### ⚙️ Tech Stack")
st.write(
    """
    - **Frontend**: Streamlit for building interactive web apps.
    - **Backend**: Mira SDK for flow management and AI integration.
    - **Environment Variables**: dotenv for secure environment configuration.
    """
)
