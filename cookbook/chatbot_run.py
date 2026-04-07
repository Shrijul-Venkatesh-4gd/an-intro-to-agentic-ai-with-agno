from agents.chatbot import chatbot

def run_chatbot_workflow():
    response = chatbot.run(
        input="I am Heisenberg. What is your name?"
    )
    print(response.content)

    response = chatbot.run(input="Say my name.")
    print(response.content)

    response = chatbot.run(input="You're goddamn right.")
    print(response.content)

run_chatbot_workflow()