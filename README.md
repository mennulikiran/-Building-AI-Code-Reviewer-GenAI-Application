# -Building-AI-Code-Reviewer-GenAI-Application
 Building AI Code Reviewer GenAI Application
AlphaBot - Python Code Reviewer
PROJECT OVERVIEW
AlphaBot is an AI-powered code reviewer application that enables developers to review Python code for bugs, logical errors, and areas of improvement. Using AlphaBot, users can submit their Python code, receive detailed feedback, and gain insights to enhance their coding practices.

KEY FEATURES
1. User-Friendly Interface
Built with Streamlit, providing an intuitive and interactive user interface.
Users can easily input Python code through a chat interface.
2. AI-Driven Code Analysis
Powered by Google Gemini AI (Generative AI) for efficient and accurate code reviews.
Feedback is categorized into:
🐞 Bug Report: Identifies potential bugs or logical flaws.
🛠️ Fixed Code: Provides optimized or corrected code snippets.
💡 Code Insights: Offers practical tips and improvements for better coding practices.
3. Interactive Chat System
Real-time conversation with the AI to review and improve Python code.
Maintains session history for seamless multi-turn interactions.
TECH STACK
✅ Frontend: Streamlit for interactive UI.
✅ Backend: Google Generative AI (Gemini 1.5 flash model).
✅ Deployment: Can be hosted locally or on any cloud platform.
HOW TO USE
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/alpha-bot-python-code-reviewer.git
cd alpha-bot-python-code-reviewer
Step 2: Install Dependencies
Install the required libraries using pip:

bash
Copy code
pip install -r requirements.txt
Step 3: Set Up the API Key
Obtain an API key from Google Cloud Console.
Replace the placeholder in the app.py file:
python
Copy code
genai.configure(api_key="YOUR_API_KEY")
Step 4: Run the Application
Start the Streamlit application:

bash
Copy code
streamlit run app.py
Step 5: Interact with AlphaBot
Enter Python code into the chat input.
Receive feedback, including bug reports, optimized code snippets, and coding insights.
