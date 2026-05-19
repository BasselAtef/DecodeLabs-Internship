import random

def ai_chatbot():
    print("Hello, I am an AI Chatbot 👋 How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower().startswith("exit") or user_input.lower().startswith("quit") or user_input.lower().startswith("bye"):
            goodbyes = ["Goodbye! 👋", "See you later!", "Bye! Have a great day! 😎"]
            print(f"AI: {random.choice(goodbyes)}")
            break
        

        elif user_input.lower().startswith("hello") or user_input.lower().startswith("hi") or user_input.lower().startswith("hey"):
            greetings = ["Hello! 👋", "Hi there! 😊", "Hey! How are you doing today? 😎"]
            print(f"AI: {random.choice(greetings)}")

        
        elif user_input.lower().startswith("thanks") or user_input.lower().startswith("thank you") or user_input.lower().startswith("ty"):
            thanks = ["You're welcome! 😊", "No problem! 😎", "My pleasure! 😄"]
            print(f"AI: {random.choice(thanks)}")    

        else:
            responses = ["I'm not sure I understand 😟", "Could you please rephrase that? 🤔", "I'm still learning, can you explain? 😅"]
            print(f"AI: {random.choice(responses)}")


if __name__ == "__main__":
    ai_chatbot()