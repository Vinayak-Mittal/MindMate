#  Mental Health Chatbot

## 🌸 Overview
The **Hinglish Mental Health Chatbot** is a conversational chatbot designed to provide emotional support and guidance in a friendly Hinglish (Hindi + English) tone. The chatbot can analyze user messages, recognize their mood, and respond with comforting, motivational, or helpful advice.

## 🚀 Features
- **Conversational AI**: Understands user input and responds with relevant, comforting messages.
- **Mood Analysis**: Detects mood based on user input (e.g., stress, happiness, anxiety, etc.).
- **Guided Meditation**: Provides a 5-minute meditation guide for relaxation.
- **Positive Affirmations**: Generates motivational messages to boost mental well-being.
- **Chat History Management**: Saves past conversations and allows clearing history.

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vinayak-Mittal/Hinglish-Mental-Health-Chatbot.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd Hinglish-Mental-Health-Chatbot
   ```
3. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate  # On Windows
   ```
4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage
1. **Run the chatbot application:**
   ```bash
   streamlit run chatbot.py
   ```
2. **Interact with the chatbot:**
   - Enter your thoughts in Hinglish, and the chatbot will respond with supportive messages.
   - Use the sidebar to get **Positive Affirmations** and **Guided Meditation**.
   - Clear chat history when needed.

## 📂 Project Structure
```
Hinglish-Mental-Health-Chatbot/
│-- chatbot.py         # Main chatbot script
│-- requirements.txt   # Required dependencies
│-- chat_history.json  # Stores conversation history
│-- README.md          # Project documentation
```

## 📌 Dependencies
- **Streamlit** (for the chatbot UI)
- **Python** (for NLP processing)
- **JSON** (for storing conversation history)
- **Datetime, Random, OS** (for handling responses and saving data)

## 🤝 Contributing
Feel free to fork this repository and submit pull requests with improvements or new features.

## 📜 License
This project is open-source and available under the **MIT License**.

## 📬 Contact
For any questions or suggestions, reach out to **[Vinayak Mittal](https://github.com/Vinayak-Mittal)**.

