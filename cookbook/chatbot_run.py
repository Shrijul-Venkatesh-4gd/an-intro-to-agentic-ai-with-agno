from agents.chatbot import chatbot


def run_chatbot_workflow():
    response = chatbot.run(
        input=(
            "Explain Kubernetes"
            "predict its future trajectory, and provide a simple example of how to use it."
        )
    )
    print(response.content)


if __name__ == "__main__":
    run_chatbot_workflow()