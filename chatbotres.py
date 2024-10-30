def chatbot_response(user_input):
    user_input = user_input.lower() #converting to lower case

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    
    elif "your name" in user_input:
        return "I'm a simple chatbot created to help you with basic queries."
    
    elif "time" in user_input:
        return "I can't tell the time yet, but I suggest you check a clock or your phone!"
    
    elif "weather" in user_input:
        return "I'm unable to check the weather, but you can look it up online!"

    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    else:
        return "I'm sorry, I don't understand. Can you ask something else?"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
