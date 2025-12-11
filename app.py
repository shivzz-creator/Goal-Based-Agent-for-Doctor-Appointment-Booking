from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

from tools.appointment_tools import extract_info, check_goal

load_dotenv()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

SYSTEM_PROMPT = """
You are a Doctor Appointment Booking Agent.

Your goal:
- Collect patient's NAME, PHONE NUMBER, DOCTOR/SPECIALIZATION, DATE, and TIME.
- Use tools to extract information.
- Use tools to check whether booking is complete.
- Once all information is collected → CONFIRM APPOINTMENT and stop.

Be polite, conversational, and guide the user naturally.
"""

tools = [
    Tool(
        name="extract_info",
        func=extract_info,
        description="Extracts name, phone number, doctor, date, and time from user message."
    ),
    Tool(
        name="check_goal",
        func=check_goal,
        description="Check if all appointment details are collected. If yes, confirm booking.",
        return_direct=True
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    agent_kwargs={"system_message": SYSTEM_PROMPT}
)

print("🩺 Hi! I'm your medical appointment assistant. How can I help you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye! Take care.")
        break

    response = agent.invoke({"input": user_input})
    print("Assistant:", response["output"])

    if "appointment booked" in response["output"].lower():
        print("\n🎉 Your appointment is successfully recorded!\n")
        break
