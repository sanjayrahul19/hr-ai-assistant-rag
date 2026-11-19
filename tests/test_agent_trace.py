
from src.agent.hr_agent import agent


def test_agent_trace():

    question = "What is employee 101's remaining leave balance?"

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    for message in response["messages"]:

        print("\nMessage type:", type(message).__name__)

        # Check whether the LLM requested a tool
        if hasattr(message, "tool_calls") and message.tool_calls:

            print("Tool calls:")

            for tool_call in message.tool_calls:
                print("Tool name:", tool_call["name"])
                print("Arguments:", tool_call["args"])

        # Check tool execution result
        elif message.type == "tool":

            print("Tool result:", message.content)

        # Check final LLM response
        elif message.type == "ai":

            print("AI response:", message.content)


if __name__ == "__main__":
    test_agent_trace()
