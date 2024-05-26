# Engineering Project Proposal Generator


## Overview

The Engineering Project Proposal Generator is a Streamlit web application designed to help users quickly generate comprehensive project proposals for engineering projects. By leveraging the Gemini API, the app generates detailed project proposals based on user inputs such as project name, description, and target audience.

## Public Streamlit App
https://mainpy-d4tatysvgwgeelcjp9hxce.streamlit.app/

## Features

- **User Input Forms**: Simple and intuitive input forms for project details.
- **AI-Generated Proposals**: Uses the Gemini API to generate a detailed project proposal.
- **Streamlined Workflow**: Ensures that all necessary fields are completed before generating a proposal.

## How It Works

1. **Enter Project Details**: Provide the project name, a detailed project description, and specify the target audience.
2. **Generate Proposal**: Click the "Generate Engineering Project Proposal" button to generate the proposal.
3. **View Proposal**: The generated proposal will be displayed on the screen.

## Installation

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Google Generative AI (`google-generativeai`)

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/engineering-project-proposal-generator.git
    cd engineering-project-proposal-generator
    ```

2. **Install the required packages**:
    ```sh
    pip install streamlit google-generativeai
    ```

3. **Set your API key**:
   Open the `app.py` file and replace `"your_api_key_here"` with your actual API key from Google.

4. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Open the Application**: Open your web browser and go to `http://localhost:8501`.
2. **Enter Project Details**:
   - **Project Name**: Enter the name of your engineering project.
   - **Project Description**: Provide a detailed description of the project.
   - **Target Audience**: Describe the target audience (e.g., engineering students, industry professionals).
3. **Generate the Proposal**: Click the "Generate Engineering Project Proposal" button.
4. **View the Proposal**: The generated project proposal will be displayed below the input fields.
