"""
Project 1: Rule-Based AI Chatbot
Goal: A simple rule-based chatbot that responds to predefined user inputs.

Key Requirements:
- Handle greetings and exit commands
- Use if-else logic for responses
- Run in a continuous loop
"""

def get_response(user_input):
    """Determine the chatbot's response using if-else logic."""
    text = user_input.lower().strip()

    # Greetings
    if text in ("hi", "hello", "hey", "hola", "yo", "good morning", "good evening"):
        return "Hello there! How can I help you today?"

    elif text in ("how are you", "how are you?", "how's it going", "hows it going"):
        return "I'm just a program, but I'm doing great! Thanks for asking."

    elif text in ("what is your name", "what's your name", "whats your name", "who are you"):
        return "I'm ChatBot, your friendly rule-based assistant."

    elif text in ("help", "what can you do"):
        return ("I can chat about simple things! Try saying 'hi', "
                "asking my name, or asking how I'm doing. "
                "Type 'bye' or 'exit' to leave.")

    elif text in ("what can you help me with", "what do you do"):
        return "I'm a simple rule-based chatbot, so I can only respond to a few set phrases. Type 'help' for ideas."

    elif "thank" in text:
        return "You're welcome!"

    elif text in ("bye", "exit", "quit", "goodbye", "see you"):
        return "EXIT"  # signal to break the loop

    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """Main loop that keeps the conversation going until the user exits."""
    print("=" * 50)
    print(" Rule-Based AI Chatbot")
    print(" Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if not user_input.strip():
            print("Bot: Please type something!")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day. 👋")
            break
        else:
            print(f"Bot: {response}")


if __name__ == "__main__":
    run_chatbot()
