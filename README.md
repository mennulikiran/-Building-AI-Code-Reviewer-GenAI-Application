# -Building-AI-Code-Reviewer-GenAI-Application
 Building AI Code Reviewer GenAI Application
# AI Code Reviewer - GenAI Application

This repository contains an AI-powered code reviewer application built using **Streamlit** and **Google's Gemini Generative AI**. The application provides conversational assistance for code reviews, helping users debug, optimize, and understand their code through an intuitive chat interface.

---

## Features

- Real-time conversational code review assistance.
- Maintains session history for seamless interactions.
- Lightweight and easy-to-deploy using Streamlit.
- Integrates with Google's Generative AI `gemini-1.5-flash` model.

---

## Prerequisites

Before running the application, ensure you have the following:

- Python 3.8 or above.
- A valid Google API key for Generative AI.
- Necessary Python dependencies (specified in `requirements.txt`).

---


## Home Page
![Screenshot 2024-11-20 201409](https://github.com/user-attachments/assets/c86231c9-c9cc-4e9a-9673-4f9147ae215f)


## Chat_Bot_Working:
![Screenshot 2024-11-20 201359](https://github.com/user-attachments/assets/341334d8-b5ed-4b3e-9250-6f2110586e15)



## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/ai-code-reviewer.git
   cd ai-code-reviewer

2. Install Dependencies Use pip to install the required libraries:

bash

**pip install -r requirements.txt**


3.Set Up Google Generative AI

Obtain an API key from Google Cloud Console.
Replace the placeholder in the **genai.configure(api_key="YOUR_API_KEY")** section with your API key.


4.Run the Application Execute the following command to start the Streamlit application:

bash
**streamlit run app.py**
Access the Application Open your browser and navigate to http://localhost:___.

