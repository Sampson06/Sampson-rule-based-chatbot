
import random
import re
from datetime import datetime

BOT_NAME = "Deco"

#  Vocabulary (the bot's "knowledge")
GREETINGS = {"hi", "hello", "hey", "hola", "namaste", "yo", "greetings"}
EXIT_WORDS = {"bye", "goodbye", "exit", "quit", "q", "cya"}
THANKS = {"thanks", "thank", "thx", "thankyou"}
POSITIVE = {"good", "great", "fine", "awesome",
            "happy", "amazing", "well", "excellent"}
NEGATIVE = {"bad", "sad", "tired", "sick",
            "terrible", "awful", "stressed", "upset"}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "There are 10 kinds of people: those who understand binary and those who don't.",
    "An if-statement walks into a bar... and checks the condition at the door.",
]


def clean(text):
    return set(re.findall(r"[a-z']+", text.lower()))


def get_reply(user_text, memory):
    words = clean(user_text)
    text = user_text.lower().strip()

    if not text:
        return "I didn't catch that. Try typing something!", True

    if words & EXIT_WORDS:
        name = memory.get("name", "friend")
        return f"Goodbye, {name}! Keep building. See you next time.", False

    #  the bot just asked a question, so interpret the answer first
    if memory.get("waiting_for") == "mood":
        memory["waiting_for"] = None
        if words & POSITIVE and not words & NEGATIVE:
            return "Glad to hear that! Positive energy makes better code.", True
        elif words & NEGATIVE:
            return "Sorry to hear that. Take a break, you deserve it. I'm here if you want to chat.", True
        else:
            return "Thanks for sharing. Want to hear a joke? Just say 'joke'.", True

    # Greetings
    if words & GREETINGS:
        if "name" in memory:
            memory["waiting_for"] = "mood"
            return f"Hello again, {memory['name']}! How are you feeling today?", True
        return f"Hello! I'm {BOT_NAME}, your rule-based assistant. What's your name?", True

    #  Name
    match = re.search(r"(?:my name is|i am|i'm|call me)\s+([a-zA-Z]+)", text)
    if match and match.group(1) not in POSITIVE | NEGATIVE:
        memory["name"] = match.group(1).capitalize()
        memory["waiting_for"] = "mood"
        return f"Nice to meet you, {memory['name']}! How are you feeling today?", True

    # Questions about the bot
    if "how" in words and "you" in words:
        return "I'm running at 100% logic. No bugs detected (yet)!", True
    elif "your" in words and "name" in words or "who" in words and "you" in words:
        return f"I'm {BOT_NAME}, a rule-based chatbot built with pure if-else logic.", True
    elif "what" in words and "do" in words and "you" in words:
        return "I follow explicit rules: greet, chat, tell jokes, share the time, and exit politely.", True

    # Utilities
    elif "time" in words:
        return f"The time is {datetime.now().strftime('%I:%M %p')}.", True
    elif "date" in words or "today" in words and "day" in words:
        return f"Today is {datetime.now().strftime('%A, %d %B %Y')}.", True
    elif "joke" in words or "funny" in words:
        return random.choice(JOKES), True
    elif "help" in words:
        return ("Try: hello, 'my name is ...', how are you, what's the time, "
                "tell me a joke, thanks, or bye to exit."), True
    elif words & THANKS:
        return "You're welcome!", True

    #  Default
    else:
        return "Hmm, I don't have a rule for that yet. Type 'help' to see what I can do.", True


def main():
    memory = {}
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'help' for ideas or 'bye' to exit.")

    #  runs until an exit command sets running
    running = True
    while running:
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Goodbye!")
            break
        reply, running = get_reply(user_text, memory)
        print(f"{BOT_NAME}: {reply}")


if __name__ == "__main__":
    main()
