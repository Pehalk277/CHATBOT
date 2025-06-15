import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK packages
nltk.download('punkt')

# Sample pairs of questions and answers
pairs = [
    ["hi|hello", ["Hello! How can I help you today?", "Hi there!"]],
    ["what is your name?", ["My name is Jarves! "]],
    ["how are you?", ["I'm doing good! What about you?"]],
    ["bye", ["Goodbye!", "See you later!"]],
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatbot
chatbot.converse()