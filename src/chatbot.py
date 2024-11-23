from .intents import RESPONSES, INTENT_PATTERNS
import random


class Chatbot:
    def detect_intent(self, user_input: str) -> str:
        # Convert input to lowercase for better matching
        user_input = user_input.lower()

        # Check each intent pattern
        for intent, patterns in INTENT_PATTERNS.items():
            if any(pattern in user_input for pattern in patterns):
                return intent

        return "unknown"

    def get_response(self, user_input: str) -> str:
        # Detect the intent
        intent = self.detect_intent(user_input)

        # Get response based on intent
        if intent in RESPONSES:
            return random.choice(RESPONSES[intent])

        return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def run(self):
        print("Bot: Hi there! Type 'quit' or 'bye' to end the chat.")

        while True:
            user_input = input("You: ").strip()

            # Check for exit conditions
            if self.detect_intent(user_input) == "farewell":
                print("Bot: Goodbye!")
                break

            response = self.get_response(user_input)
            print(f"Bot: {response}")
