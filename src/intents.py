from typing import Dict, List
import random

# Define multiple responses for each intent to make the bot more varied
RESPONSES: Dict[str, List[str]] = {
    "greeting": [
        "Hello! How can I assist you today?",
        "Hi there! What can I do for you?",
        "Greetings! How may I help you?",
    ],
    "farewell": [
        "Goodbye! Have a great day!",
        "See you later! Take care!",
        "Bye! Hope to chat again soon!",
    ],
    "ask_time": [
        "Sorry, I cannot provide the current time.",
        "I'm not able to tell the time yet.",
        "Time-telling isn't one of my features.",
    ],
    "help": [
        "I can help with basic conversation. Try greeting me or asking questions!",
        "I'm a simple chatbot. I can respond to greetings and farewells.",
        "Need help? Just try talking to me naturally!",
    ],
}

# Define keyword mappings for each intent
INTENT_PATTERNS: Dict[str, List[str]] = {
    "greeting": ["hello", "hi", "hey", "greetings", "good morning", "good afternoon"],
    "farewell": ["bye", "goodbye", "see you", "farewell", "exit", "quit"],
    "ask_time": ["time", "clock", "hour"],
    "help": ["help", "assist", "support", "what can you do"],
}
