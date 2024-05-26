import streamlit as st
import google.generativeai as genai

# Set your API key here directly
API_KEY = "AIzaSyALhFcwj6SEH6t5rswdIiEyNezeQJjr398"

# Configure API Keys
genai.configure(api_key=API_KEY)

# Generate engineering project proposal prompt for the Gemini API
def generate_engineering_project_proposal(project_name, project_description, target_audience):
    prompt = f"""
    Generate An Engineering Project Proposal

    Project Name: {project_name}

    Project Description:
    {project_description}

    Target Audience:
    {target_audience}

    Briefly outline the key components of the engineering project proposal including goals, objectives, resources needed, and assessment methods.
    """
    return prompt

@st.cache_data
def generate_engineering_project_response(project_name, project_description, target_audience):
    # model configurations
    model = genai.GenerativeModel("gemini-1.5-flash")
    model.temperature = 0.8
    model.top_k = 20
    model.top_p = 0.7
    model.max_output_tokens = 500

    # Provide a prompt for generation
    prompt = generate_engineering_project_proposal(project_name, project_description, target_audience)

    # Generate content
    response = model.generate_content([prompt])

    return response.text

def app():
    st.title("Engineering Project Proposal Generator")
    st.markdown("**Developed by: Gabriel Constantine B. Belandres**")
    st.text("")

    project_name = st.text_input("Enter project name:")
    st.text("")

    project_description = st.text_area("Enter project description(Explain the details):")
    st.text("")

    target_audience = st.text_area("Describe the target audience (e.g., engineering students, industry professionals, general public):")
    st.text("")

    if st.button("Generate Engineering Project Proposal"):
        if project_name and project_description and target_audience:
            project_response = generate_engineering_project_response(project_name, project_description, target_audience)
            st.write(project_response)
        else:
            st.error("Fill out all the required fields.")


app()
