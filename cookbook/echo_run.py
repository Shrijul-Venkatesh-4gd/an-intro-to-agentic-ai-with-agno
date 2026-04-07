from agents.echo import echo

def run_echo_workflow():
    response = echo.run(input="Hi there! How are you doing today?")
    print(response.content)

run_echo_workflow()