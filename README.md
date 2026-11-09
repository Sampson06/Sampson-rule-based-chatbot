# Rule-Based AI Chatbot 🤖

A simple rule-based chatbot built with Python for DecodeLabs Project 1.

This project demonstrates the foundation of AI interaction systems using explicit control flow instead of machine learning. The chatbot reads user input, normalizes it, matches it against predefined rules using `if-elif-else` logic, and returns the appropriate response inside a continuous loop.

## 📌 Project Goal

Create a rule-based AI chatbot that responds to predefined user inputs, handles greetings and exit commands, and runs continuously until the user chooses to exit.

## ✨ Features

- Handles greetings such as `hello`, `hi`, `hey`, etc.
- Supports exit commands such as `bye`, `exit`, `quit`, `goodbye`, and `stop`
- Uses `if-elif-else` decision-making logic
- Runs in a continuous loop until the user exits
- Normalizes input by lowercasing, trimming spaces, and removing punctuation
- Includes help, motivation, jokes, AI-related questions, and small-talk responses
- Handles empty input safely
- Extensible structure for adding more rules and smarter nested conditions

## 🧠 Key Concepts Covered

- Control flow
- Decision-making logic
- Rule-based systems
- Input normalization
- Basic human-computer interaction
- Deterministic response generation
- Foundational AI concepts

## 🛠️ Tech Stack

- Python 3
- Standard library only
- No external dependencies required

## 📁 Project Structure

```text
rule-based-ai-chatbot/
│
├── chatbot.py
└── README.md
