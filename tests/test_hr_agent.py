
from src.agent.hr_agent import ask_hr_assistant


def test_hr_agent():

    questions = [
        "How many casual leaves are allowed annually?",
        "What is employee 101's department?",
        "What is employee 101's remaining leave balance?"
    ]

    for question in questions:

        print("\n" + "=" * 60)
        print("USER:", question)

        answer = ask_hr_assistant(question)

        print("\nHR ASSISTANT:", answer)


if __name__ == "__main__":
    test_hr_agent()
