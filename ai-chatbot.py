import random

def ai_chatbot():
    print("Hello, I am an AI Chatbot 👋 How can I help you today?")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ("exit", "quit", "bye", "goodbye", "good bye"):
            goodbyes = ["Goodbye! 👋", "See you later!", "Bye! Have a great day! 😎"]
            print(f"AI: {random.choice(goodbyes)}")
            break
        

        elif any(word in user_input for word in ("hello", "hi", "hey", "greetings")):
            greetings = ["Hello! 👋", "Hi there! 😊", "Hey! How are you doing today? 😎"]
            print(f"AI: {random.choice(greetings)}")

        
        elif any(word in user_input for word in ("thanks", "thank you", "ty")):
            thanks = ["You're welcome! 😊", "No problem! 😎", "My pleasure! 😄"]
            print(f"AI: {random.choice(thanks)}")    

        else:
            responses = ["I'm not sure I understand 😟", "Could you please rephrase that? 🤔", "I'm still learning, can you explain? 😅"]
            print(f"AI: {random.choice(responses)}")


if __name__ == "__main__":
    ai_chatbot()