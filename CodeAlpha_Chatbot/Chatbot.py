def chatbot_bot(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi! Nice to meet you."
    elif user_input == "how are you":
        return "I'm fine, thanks for asking."
    elif user_input == "what is your name":
        return "I am a simple Python chatbot."
    elif user_input == "help":
        return "You can say hello, how are you, or bye."
    elif user_input == "bye":
        return "Goodbye! Have a nice day."
    else:
        return "Sorry, I don't understand that."
print("Simple Chatbot Started")
print("Type 'bye' to exit")
while True:
    user = input("You: ")
    response = chatbot_bot(user)
    print("Bot:", response)
    if user.lower() == "bye":
        break
