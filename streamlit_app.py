import streamlit as st
import json
from datetime import datetime
import random
import os

# Page configuration
st.set_page_config(page_title="Hinglish Mental Health Chatbot")

# Initialize session state for conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

class MentalHealthChatbot:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Namaste! Kaise ho aap?",
                "Hello! Kaisa chal raha hai?",
                "Hi! Aaj ka din kaisa ja raha hai?"
            ],
            "stress": [
                "Main samajh sakti hun. Stress bohot common hai. Deep breathing try karo",
                "Tension mat lo. Kuch relaxing activities try karte hain",
                "Aapko stress feel ho raha hai? Chalo meditation karte hain"
            ],
            "sad": [
                "It's okay to feel sad. Baat share karna chahte ho?",
                "Main hun na aapke saath. Kya hua?",
                "Sadness temporary hai. Aap strong ho"
            ],
            "anxiety": [
                "Anxiety normal hai. Deep breaths lo - 4 seconds in, 4 seconds out",
                "Abhi present moment pe focus karo. Sab theek ho jayega",
                "Anxiety ke time grounding exercises help karti hain"
            ],
            "happy": [
                "Bahut accha! Khush rehna important hai",
                "Your happiness makes me happy! Aisa hi positive rehna",
                "That's great! Ye khushi barkarar rakho"
            ],
            "default": [
                "Main samajh nahi paayi. Aur detail mein batayenge?",
                "Thoda aur explain kar sakte ho?",
                "I'm here to listen. Aage bolo"
            ]
        }
        self.history_file = "chat_history.json"
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        else:
            self.history = []

    def save_history(self):
        with open(self.history_file, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def analyze_mood(self, user_input):
        user_input = user_input.lower()
        if any(word in user_input for word in ["hi", "hello", "namaste", "hey"]):
            return "greeting"
        elif any(word in user_input for word in ["stress", "tension", "pareshan"]):
            return "stress"
        elif any(word in user_input for word in ["sad", "dukhi", "upset"]):
            return "sad"
        elif any(word in user_input for word in ["anxiety", "ghabrahat", "dar"]):
            return "anxiety"
        elif any(word in user_input for word in ["happy", "khush", "accha"]):
            return "happy"
        return "default"

    def get_response(self, user_input):
        mood = self.analyze_mood(user_input)
        response = random.choice(self.responses[mood])
        
        # Save to history
        chat_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_input,
            "bot": response
        }
        
        self.history.append(chat_entry)
        self.save_history()
        
        return response

    def generate_affirmation(self):
        affirmations = [
            "Aap bohot strong hain. Har mushkil se deal kar sakte hain!",
            "Har din ek naya mauka hai. Aap amazing ho!",
            "Aapke andar bahut potential hai. Believe in yourself!",
            "You are worthy of all good things. Khud pe bharosa rakho!",
            "Aap jahan bhi ho, perfect position pe ho. Keep growing!"
        ]
        return random.choice(affirmations)

    def generate_meditation_guide(self):
        return """5-Minute Meditation Guide:

1. Comfortable position mein baith jaiye (1 minute)
   - Aankhen band kar lijiye
   - Deep breath lijiye

2. Breathing pe focus karein (2 minute)
   - 4 seconds ke liye saans andar
   - 4 seconds ke liye saans bahar
   - Repeat

3. Body ko relax karein (1 minute)
   - Har muscle ko dhela chod dijiye
   - Tension release karein

4. Peaceful thoughts (1 minute)
   - Koi peaceful jagah imagine karein
   - Positive feelings pe focus karein

Remember: Thoughts aaye toh aane dijiye, bas observe karein aur jaane dijiye."""

def main():
    st.title("🌸 Hinglish Mental Health Support Chatbot")
    st.write("Aap se baat karke mujhe khushi hogi! (I'm happy to talk with you!)")

    # Initialize chatbot
    chatbot = MentalHealthChatbot()

    # Display chat history
    for msg in st.session_state.conversation_history:
        with st.chat_message("user"):
            st.write(msg["user"])
        with st.chat_message("assistant"):
            st.write(msg["bot"])

    # Chat input
    user_input = st.chat_input("Apne thoughts share karein... (Share your thoughts...)")
    
    if user_input:
        # Add user message to chat
        with st.chat_message("user"):
            st.write(user_input)

        # Get and display bot response
        bot_response = chatbot.get_response(user_input)
        with st.chat_message("assistant"):
            st.write(bot_response)

        # Update session state
        st.session_state.conversation_history.append({
            "user": user_input,
            "bot": bot_response
        })

    # Sidebar with additional features
    with st.sidebar:
        st.header("Additional Support")
        
        if st.button("🌟 Positive Affirmation"):
            affirmation = chatbot.generate_affirmation()
            st.success(affirmation)
            
        if st.button("🧘‍♀️ Guided Meditation"):
            meditation = chatbot.generate_meditation_guide()
            st.info(meditation)
            
        if st.button("🗑️ Clear Chat History"):
            st.session_state.conversation_history = []
            if os.path.exists(chatbot.history_file):
                os.remove(chatbot.history_file)
            st.rerun()

if __name__ == "__main__":
    main()
