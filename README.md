# Rule-Based AI Chatbot

A simple, elegant **rule-based chatbot** built entirely in Python — no external libraries, no APIs, just clean logic. It's designed as a beginner-friendly introduction to the core building blocks behind every AI conversational system.

---

## 📖 Project Description

This chatbot responds to predefined user inputs using classic **rule-based logic** — no machine learning, no NLP models, just Python fundamentals doing the heavy lifting.

It's built using:
- **Conditional statements** (`if / elif / else`) to decide how to respond
- **Loops** to keep the conversation running continuously
- **String handling** to normalize and match user input

The goal isn't sophistication — it's clarity. This project is meant to make the *mechanics* of a chatbot visible and understandable before layering on any complexity.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👋 Greeting responses | Recognizes common greetings like "hi," "hello," "hey" |
| ❓ Predefined questions | Handles questions about the bot's name, mood, and capabilities |
| 🚪 Exit commands | Ends gracefully on "bye," "exit," or "quit" |
| 🔤 Case-insensitive input | Works whether you type "HI," "Hi," or "hi" |
| 🔁 Continuous conversation loop | Keeps chatting until the user chooses to leave |
| 🌱 Beginner-friendly implementation | Clean, readable, well-commented code |

---

## 🛠️ Technologies Used

- **Python 3** — the only dependency; no external packages required

---

## 🎯 Project Goals

Create a simple rule-based chatbot that can:
- Interpret basic user input
- Respond appropriately using conditional logic
- Run continuously in a conversational loop until the user exits

---

## 🧠 Key Skills Demonstrated

- Control Flow
- Decision Making
- Functions
- Loops
- String Manipulation
- Problem Solving
- Basic AI Concepts

---

## 📂 Project Structure

```
decodelabs-rulebased-chatbot/
├── rule_based_chatbot.py   # Main chatbot script
└── README.md               # Project documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/ajwaahmed-ai/decodelabs-rulebased-chatbot.git
cd decodelabs-rulebased-chatbot
```

No external dependencies are required — just a working Python 3 installation.

---

## ▶️ Usage

Run the chatbot directly with Python:

```bash
python3 rule_based_chatbot.py
```

Then just start chatting! Type `bye`, `exit`, or `quit` whenever you're ready to end the conversation.

---

## 💬 Example Conversation

```
==================================================
 Rule-Based AI Chatbot
 Type 'bye', 'exit', or 'quit' to end the chat.
==================================================

You: hi
Bot: Hello there! How can I help you today?

You: what is your name
Bot: I'm ChatBot, your friendly rule-based assistant.

You: how are you
Bot: I'm just a program, but I'm doing great! Thanks for asking.

You: thanks
Bot: You're welcome!

You: bye
Bot: Goodbye! Have a great day. 👋
```

---

## 🔍 How It Works

<details>
<summary>Click to expand the internal logic breakdown</summary>

<br>

The chatbot's brain lives in a single function: **`get_response()`**.

1. The user's input is lowercased and stripped of extra whitespace, so "Hi", "HI", and " hi " are all treated the same.
2. A chain of `if / elif / else` statements checks the cleaned input against sets of known phrases.
3. Depending on the match, the function returns an appropriate string response — or a special `"EXIT"` signal if the user wants to leave.
4. The **main loop**, `run_chatbot()`, continuously prompts the user with `input()`, passes it to `get_response()`, and prints the result — repeating indefinitely until the exit signal is returned, at which point the loop `break`s and the program ends.

This structure — input → normalize → match → respond → loop — is the same conceptual backbone used in far more advanced conversational AI systems, just without the statistical modeling.

</details>

---

## 🔮 Future Improvements

- 🧩 Support for more intents and conversational topics
- 🔎 Regular expressions for more flexible input matching
- 🧠 NLP integration (e.g. spaCy, NLTK) for smarter understanding
- 🤖 Machine learning-based intent classification
- 🗂️ Persistent conversation history
- 🖥️ Graphical user interface (GUI) version
- 🎙️ Voice assistant capabilities
- 🌐 API integration for external data/services
- 🚀 Web-based version using Flask or FastAPI

---

## 🎓 Learning Outcomes

By building and studying this project, you'll come away with hands-on experience in:
- Writing and structuring functions in Python
- Using conditional logic to drive program behavior
- Implementing loops for continuous, interactive programs
- Cleaning and normalizing string input
- Thinking through the fundamental design of conversational systems

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.
