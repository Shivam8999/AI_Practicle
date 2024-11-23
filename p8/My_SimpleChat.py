print("Simple Question and Answering Program")
print("=====================================")
print("You may ask any one of these questions:")
print("1. Hi")
print("2. How are you?")
print("3. Are you working?")
print("4. What is your name?")
print("5. What did you do yesterday?")
print("6. Quit")

while True:
    question = input("Enter one question from the above list: ").lower()

    if question == 'hi':
        print("Hello!")
        break
    elif question == 'how are you':
        print("I am fine, thank you!")
        break
    elif question in ['are you working?', 'are you doing any job?']:
        print("Yes, I am working at KLU.")
        break
    elif question == 'what is your name?':
        print("My name is Emilia.")
        name = input("Enter your name: ")
        print(f"Nice to meet you, {name}!")
        break
    elif question == 'what did you do yesterday?':
        print("I watched Bahubali 5 times!")
        break
    elif question == 'quit':
        print("Goodbye!")
        break
    else:
        print("I don't understand what you said. Please ask a question from the list.")
