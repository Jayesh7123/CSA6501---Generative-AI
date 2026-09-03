README – Context-Aware Chatbot
1. Project Title
Context-Aware Chatbot Using LangChain and LLM

2. Description
This project implements a context-aware chatbot using LangChain and a Large Language Model (LLM).

The chatbot maintains the previous conversation history and uses it as context while answering new questions. This allows the chatbot to understand follow-up queries and provide more relevant responses.

3. Features
Accepts questions from the user through the console.

Uses LangChain to interact with the LLM.

Maintains previous conversation history.

Uses previous questions and answers as context.

Supports follow-up questions.

Provides clear and concise responses.

Handles empty input and errors.

Allows the user to exit the conversation using exit.

4. Technologies Used
Python

LangChain

OpenAI LLM

python-dotenv

5. Project Structure

context-aware-chatbot/
│
├── context_aware_chatbot.py
├── .env
└── README.md
6. Requirements
Install the required Python packages:

Bash

pip install langchain langchain-openai python-dotenv
7. API Configuration
Create a file named .env in the same folder as the Python program.

Add:


OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-4o-mini
Replace your_api_key with your valid OpenAI API key.

8. How to Run
Open the project folder in VS Code terminal and run:

Bash

python context_aware_chatbot.py
The chatbot will start in the terminal.

9. Sample Input

User: What is supervised learning?

User: Give an example of supervised learning.
10. Sample Output

Context-Aware Chatbot
Type 'exit' to stop.

User: What is supervised learning?

Chatbot: Supervised learning is a machine learning method
where a model learns from labelled training data.

User: Give an example of supervised learning.

Chatbot: Email spam detection is an example of supervised
learning because the model learns from emails labelled as
spam or not spam.
11. Working Principle

User Query
     ↓
Conversation History
     ↓
Context Creation
     ↓
Prompt Construction
     ↓
LangChain LLM
     ↓
Generated Response
     ↓
Store Response
     ↓
Next User Query
12. Conclusion
The Context-Aware Chatbot successfully uses LangChain, conversation history, and an LLM to generate relevant responses. By using previous questions and answers as context, the chatbot can understand follow-up queries and provide more meaningful responses.
