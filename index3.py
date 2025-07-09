mport nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello there!", "Hi! How can I assist you today?", "Hey! How are you doing?"]],
    [r"how are you ?", ["I'm just a bot, but I'm doing well!", "I'm functioning as expected."]],
    [r"what is your name ?", ["I'm CODTECH Bot, your AI assistant!"]],
    [r"who created you ?", ["I was developed by a CODTECH intern using Python and NLP."]],
    [r"what can you do ?", [
        "I can answer simple questions, respond to greetings, and help you get started with basic NLP.",
        "I am built to respond to certain inputs using predefined rules."]],
    [r"can you learn ?", [
        "In this version, I don't learn, but you can train me by adding more patterns!",
        "Nope, I'm a rule-based chatbot. For learning, you need a machine learning model."]],
    [r"what is NLP ?", [
        "NLP stands for Natural Language Processing. It's a field of AI focused on understanding and generating human language.",
        "Natural Language Processing allows computers to understand and respond to human language."]],
    [r"tell me a joke", [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer go to the doctor? Because it had a virus!"]],
    [r"how to learn python ?", [
        "Start with basics at w3schools or Codecademy. Practice daily!",
        "You can use YouTube tutorials, freeCodeCamp, or books like 'Automate the Boring Stuff with Python'."]],
    [r"bye|exit|quit", ["Goodbye! Have a great day!", "Bye! Hope to chat with you soon."]],
]

def fallback_response(user_input):
    return "Sorry, I didn't understand that. Can you rephrase?"

def codtech_chatbot():
    print("CODTECH Chatbot is now online! (type 'bye' to exit)\n")
    chatbot = Chat(pairs, reflections)
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        response = chatbot.respond(user_input)
        if response:
            print(f"Bot: {response}")
        else:
            print(f"Bot: {fallback_response(user_input)}")

if __name__ == "__main__":
    codtech_chatbot()
