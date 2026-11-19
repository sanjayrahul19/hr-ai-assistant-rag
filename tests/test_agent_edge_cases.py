
from src.agent.hr_agent import ask_hr_assistant


def test_agent_edge_cases():

    questions = [
        "What is my remaining leave balance?",
        "What is the maternity leave policy?",
        "Show employee 999's details."
    ]

    for question in questions:

        print("\n" + "=" * 60)
        print("USER:", question)

        answer = ask_hr_assistant(question)

        print("\nHR ASSISTANT:", answer)


if __name__ == "__main__":
    test_agent_edge_cases()
