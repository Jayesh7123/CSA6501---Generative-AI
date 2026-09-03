import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    print("OPENAI_API_KEY is not configured.")
    print("Create a .env file and add:")
    print("OPENAI_API_KEY=your_api_key")
    print("OPENAI_MODEL=gpt-4o-mini")
    raise SystemExit

llm = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    temperature=0,
    api_key=API_KEY
)

conversation_history = []

print("Context-Aware Chatbot")
print("Type 'exit' to stop.")

while True:
    user_query = input("\nUser: ")

    if user_query.lower() == "exit":
        print("Chatbot: Conversation ended.")
        break

    if not user_query.strip():
        print("Chatbot: Please enter a valid question.")
        continue

    context = ""

    for question, answer in conversation_history:
        context += f"Previous User: {question}\n"
        context += f"Previous Assistant: {answer}\n"

    prompt = f"""
You are a context-aware engineering assistant.

Use the previous conversation context when it is relevant.

Previous Conversation:
{context}

Current User Question:
{user_query}

Give a clear and concise answer.
"""

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        answer = response.content

        print(f"\nChatbot: {answer}")

        conversation_history.append((user_query, answer))

    except Exception as error:
        print(f"Chatbot: Error while generating response: {error}")
