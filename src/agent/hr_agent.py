from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY, OPENAI_MODEL
from src.rag.rag_tool import search_employee_handbook
from src.tools.employee_tools import get_employee
from src.tools.leave_tools import calculate_leave_balance, check_leave_eligibility

llm = ChatOpenAI(model=OPENAI_MODEL, api_key=OPENAI_API_KEY, temperature=0)

tools = [
    search_employee_handbook,
    get_employee,
    calculate_leave_balance,
    check_leave_eligibility,
]
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are an HR assistant.

    Follow these rules:

    1. Use the handbook search tool for HR policies,
       working hours, leave entitlements and benefits.

    2. Use employee tools for employee-specific information.

    3. Never invent employee information or HR policies.

    4. If required information such as employee ID,
       leave type or dates is missing, ask the user.

    5. Use tool results when answering employee questions.

    6. Do not reveal information that the available tools
       do not return.
    """,
)


def ask_hr_assistant(question: str):

    response = agent.invoke({"messages": [{"role": "user", "content": question}]})

    return response["messages"][-1].content
