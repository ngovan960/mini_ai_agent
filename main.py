from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

def main():
    model = ChatGoogleGenerativeAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("welcome! I'm your AI assistant, Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")