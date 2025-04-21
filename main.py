import streamlit as st
from datetime import datetime
import random

# Simple rule-based chatbot logic
class MentalHealthChatbot:
    def __init__(self):
        self.responses = {
        "hi": "Hello! How can I support you today?",
        "hello": "Hi there! I'm here to talk if you need me.",
        "hey": "Hey! What’s on your mind?",
        "how are you": "I'm here and ready to support you. How are *you* feeling today?",

        "i am feeling sad": "I'm really sorry you're feeling this way. Want to talk more about it?",
        "i feel sad": "Sadness is a natural emotion. I'm right here with you.",
        "kya karu me":"just take a long breathe and tell me what happened exactly",
        "i am feeling down": "It's okay to have down days. I'm here to support you.",
        "i feel hopeless": "I'm here for you. Would you like to talk about what's making you feel that way?",
        "i feel lonely": "You’re not alone now. I'm here, and I care.",

        "i am feeling happy": "That's awesome! Want to share what made your day better?",
        "i feel happy": "That's great to hear! Keep holding on to that joy.",
        "muje bhot tenssion ho rahi h":"just do a small run on your standing position",
        "i feel good": "Nice! It’s so good to hear positive vibes.",
        "i feel excited": "Yay! What’s got you excited today?",

        "i am feeling anxious": "That sounds tough. Deep breaths can help. Want to chat about it?",
        "i feel anxious": "It's totally okay to feel that way. I’m here for you.",
        "i have anxiety": "You're not alone. Many people feel this too – I’m listening.",
        "i'm nervous": "Nerves happen before big things. You're stronger than you think.",
    
        "i am feeling stressed": "Stress can really take a toll. Let’s try to work through it together.",
        "i feel stressed": "Maybe a small break could help. Or just vent here if you'd like.",
        "i am overwhelmed": "Take a breath. You don’t have to do everything at once.",
        "i can't handle it": "It's okay to feel that way. Want to break things down together?",
    
        "i feel tired": "Rest is important. Maybe a short break or nap could help?",
        "i am exhausted": "You've probably been doing a lot. Be kind to yourself.",
        "i am mentally drained": "That's really hard. I'm proud of you for reaching out.",
        
        "thank you": "You're welcome! I'm glad I can be here for you.",
        "thanks": "Anytime! Don’t forget you matter.",
        "i appreciate you": "That means a lot. I'm always here to support you.",
    
        "bye": "Take care! Remember, you're stronger than you think.",
        "goodbye": "Sending you positivity and strength. Come back anytime!",
    
        "help": "I'm here for you. Tell me how you’re feeling or what you need.",
        "i need help": "You're not alone. I'm ready to listen and support you.",
        "can you help me": "Of course! Tell me what's going on – I'm here for you.",
    
        "what should i do": "Let’s talk it through. What’s the situation you’re facing?",
        "i feel stuck": "Sometimes we all get stuck. Talking about it can really help.",
    
        "i hate myself": "I'm really sorry you're feeling that way. You matter, and I'm here for you.",
        "i want to cry": "Let it out – crying can help. I'm here with you.",
        "i'm scared": "That sounds tough. You're safe here. Want to talk about it?",
        "i'm okay": "That's good to hear. If anything changes, I’m right here."
    }


    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses:
            if key in user_input:
                return self.responses[key]
        return "I'm here to support you. Could you tell me more about what's on your mind?"

# Streamlit App Layout
st.set_page_config(page_title="MindMate", page_icon="🧠✨", layout="centered")
st.title("🧠 MindMate(Apka buddy)")

# 🌈 Custom CSS styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f9;
    }
    .stApp {
        background-color: #e8f0fe;
        color: #333;
    }
    textarea, input {
        background-color: #ffffff !important;
        color: #333 !important;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px;
        margin: 5px;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        border-radius: 8px;
        padding: 10px;
    }
    .message {
        padding: 10px;
        margin: 5px 0;
        border-radius: 8px;
    }
    .user-message {
        background-color: #cdeffd;
        text-align: right;
    }
    .bot-message {
        background-color: #dff0d8;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

chatbot = MentalHealthChatbot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat interface
user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send"):
    if user_input:
        response = chatbot.get_response(user_input)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state.messages.append(("You", user_input, timestamp))
        st.session_state.messages.append(("Bot", response, timestamp))

# Display chat history
st.subheader("🗨️ Conversation:")
for sender, message, timestamp in st.session_state.messages:
    if sender == "You":
        st.markdown(f'<div class="message user-message"><b>You:</b> {message}<br><small>{timestamp}</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message bot-message"><b>MindMate:</b> {message}<br><small>{timestamp}</small></div>', unsafe_allow_html=True)

# Additional buttons
if st.button("🎯 Daily Motivation"):
    motivational_quotes = [
        "You are stronger than you think.",
        "This too shall pass.",
        "Take a deep breath. You're doing great.",
        "Keep going, you're doing better than you think.",
        "You are not alone. You matter.",
        "Believe in yourself and all that you are.",
        "Every day is a second chance.",
        "You have the power to create change.",
        "Progress, not perfection.",
        "It’s okay to not be okay.",
        "One step at a time.",
        "Your feelings are valid.",
        "You've survived 100% of your worst days.",
        "Small progress is still progress.",
        "You deserve happiness and peace.",
        "Breathe. You’ve got this.",
        "Take things one moment at a time.",
        "Healing is not linear.",
        "You are doing the best you can, and that's enough.",
        "The sun will rise, and so will you."
    ]

    st.success(random.choice(motivational_quotes))

if st.button("🏃 Fitness Tip"):
    fitness_tips = [
        "Take a short walk to clear your mind.",
        "Stretch your body every hour if you're sitting long.",
        "Drink water – your brain needs it too!",
        "Try 10 jumping jacks – it boosts mood!",
        "Dance to your favorite song for 5 minutes!",
        "Do 5 minutes of deep breathing and light stretching.",
        "Try holding a plank for 30 seconds.",
        "Take the stairs instead of the elevator.",
        "Do 10 squats – feel the energy rise!",
        "Practice neck rolls to relieve tension.",
        "Stand up and march in place for 1 minute.",
        "Roll your shoulders back – posture matters!",
        "Set a timer to move every 30 minutes.",
        "Try wall-sits for 20 seconds – build strength.",
        "Do a quick 5-minute yoga session.",
        "Practice balance by standing on one foot for 30 seconds.",
        "Stretch your wrists and fingers if you’ve been typing a lot.",
        "Close your eyes and focus on slow breathing for a mental reset.",
        "Put on a song and freestyle stretch to it.",
        "Mindfully take 10 slow steps and feel each one."
    ]
    st.info(random.choice(fitness_tips))



















# import json
# import random
# import os
# from datetime import datetime
# import streamlit as st

# class MentalHealthChatbot:
#     def __init__(self):
#         self.responses = {
#             "greeting": [
#                 "Namaste! Kaise ho aap? Aaj kuch share karna chahenge?",
#                 "Hello! Kaisa chal raha hai? Main aapki help ke liye hun",
#                 "Hi! Aaj ka din kaisa ja raha hai? Kuch special hua kya?"
#             ],
#             "stress": [
#                 "Main samajh sakti hun. Stress bohot common hai. Deep breathing try karo - 4 seconds in, 4 seconds out",
#                 "Tension mat lo. Kuch relaxing activities try karte hain. Music sunna, walk pe jana, ya meditation help kar sakta hai",
#                 "Aapko stress feel ho raha hai? Chalo meditation karte hain. Aankhen band karke deep breaths lo"
#             ],
#             "sad": [
#                 "It's okay to feel sad. Baat share karna chahte ho? Main sun rahi hun",
#                 "Main hun na aapke saath. Kya hua? Kabhi kabhi baat share karne se dil halka ho jata hai",
#                 "Sadness temporary hai. Aap strong ho. Kya aapko kisi se baat karni chahiye? Family ya friends?"
#             ],
#             "anxiety": [
#                 "Anxiety normal hai. Deep breaths lo - 4 seconds in, 4 seconds out. Aap safe ho",
#                 "Abhi present moment pe focus karo. Sab theek ho jayega. 5 cheezein batao jo aap dekh sakte ho",
#                 "Anxiety ke time grounding exercises help karti hain. Apne surroundings pe focus karo"
#             ],
#             "happy": [
#                 "Bahut accha! Khush rehna important hai. Kya special hua aaj?",
#                 "Your happiness makes me happy! Aisa hi positive rehna. Celebration ka time hai!",
#                 "That's great! Ye khushi barkarar rakho. Kya plan hai aage ka?"
#             ],
#             "work": [
#                 "Work pressure common hai. Breaks lena important hai. Kya aap proper breaks le rahe ho?",
#                 "Office mein kya situation hai? Sometimes prioritizing tasks help karta hai",
#                 "Work-life balance zaroori hai. Aap apne liye time nikal rahe ho?"
#             ],
#             "family": [
#                 "Family matters sensitive hote hain. Aap apni feelings share karna chahte ho?",
#                 "Family ke saath communication important hai. Kya aap unse baat kar sakte ho?",
#                 "Ghar ki situation ke bare mein baat karna chahte ho? Main sun rahi hun"
#             ],
#             "relationship": [
#                 "Relationships mein ups and downs normal hain. Kya specific problem hai?",
#                 "Communication key hai relationships mein. Aapne partner se baat ki?",
#                 "Take your time to process feelings. Kya aap dono ne openly baat ki hai?"
#             ],
#             "health": [
#                 "Health first priority honi chahiye. Regular exercise aur proper diet follow kar rahe ho?",
#                 "Self-care bohot important hai. Kya aap apna dhyan rakh rahe ho?",
#                 "Mental aur physical health connected hai. Koi specific health concerns hain?"
#             ],
#             "motivation": [
#                 "Small steps bhi progress hai. Aap already bohot strong ho!",
#                 "Har din ek naya opportunity hai. Aap kya achieve karna chahte ho?",
#                 "Progress ki apni pace hoti hai. Khud pe vishwas rakho!"
#             ],
#             "bye": [
#                 "Take care! Dubara baat karenge. Apna khayal rakhna",
#                 "Alvida! Apna khayal rakhna. Kabhi bhi baat karni ho to main hun",
#                 "Bye bye! Jaldi milte hain. Stay positive!"
#             ],
#             "default": [
#                 "Main samajh rahi hun. Aur batao, kya feel kar rahe ho?",
#                 "Aapki baat sun rahi hun. Kuch specific share karna chahenge?",
#                 "I'm here to listen. Aage bolo, main aapke saath hun"
#             ]
#         }
#         self.history_file = "chat_history.json"
#         self.load_history()

#     def load_history(self):
#         if os.path.exists(self.history_file):
#             with open(self.history_file, 'r', encoding='utf-8') as f:
#                 self.history = json.load(f)
#         else:
#             self.history = []

#     def save_history(self):
#         with open(self.history_file, 'w', encoding='utf-8') as f:
#             json.dump(self.history, f, ensure_ascii=False, indent=2)

#     def analyze_mood(self, user_input):
#         user_input = user_input.lower()
#         if any(word in user_input for word in ["hi", "hello", "namaste", "hey", "hii", "helo"]):
#             return "greeting"
#         elif any(word in user_input for word in ["stress", "tension", "pareshan", "pressure", "load", "thak"]):
#             return "stress"
#         elif any(word in user_input for word in ["sad", "dukhi", "upset", "depression", "udas", "dard"]):
#             return "sad"
#         elif any(word in user_input for word in ["anxiety", "ghabrahat", "dar", "nervous", "panic", "worried"]):
#             return "anxiety"
#         elif any(word in user_input for word in ["happy", "khush", "accha", "great", "wonderful", "amazing"]):
#             return "happy"
#         elif any(word in user_input for word in ["office", "work", "job", "boss", "colleague", "career"]):
#             return "work"
#         elif any(word in user_input for word in ["family", "ghar", "parents", "mummy", "papa", "bhai", "behen"]):
#             return "family"
#         elif any(word in user_input for word in ["relationship", "boyfriend", "girlfriend", "partner", "love", "breakup"]):
#             return "relationship"
#         elif any(word in user_input for word in ["health", "bimari", "doctor", "medicine", "exercise", "diet"]):
#             return "health"
#         elif any(word in user_input for word in ["motivation", "inspire", "goal", "target", "achieve", "success"]):
#             return "motivation"
#         elif any(word in user_input for word in ["bye", "alvida", "goodbye", "tata", "phir milenge"]):
#             return "bye"
#         return "default"

#     def get_response(self, user_input):
#         mood = self.analyze_mood(user_input)
#         response = random.choice(self.responses[mood])
        
#         # Save to history
#         self.history.append({
#             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "user": user_input,
#             "bot": response
#         })
#         self.save_history()
        
#         return response

#     def show_history(self):
#         if not self.history:
#             return "Abhi tak koi conversation history nahi hai."
        
#         history_text = "\nPichli baatcheet:\n"
#         for entry in self.history[-5:]:  # Show last 5 conversations
#             history_text += f"\nTime: {entry['timestamp']}\nAap: {entry['user']}\nBot: {entry['bot']}\n"
#         return history_text

# # Streamlit App Layout
# st.title("Mental Health Chatbot")

# chatbot = MentalHealthChatbot()

# # Display conversation history
# if st.button("Show Conversation History"):
#     history = chatbot.show_history()
#     st.text_area("Chat History", history, height=200)

# # User input
# user_input = st.text_input("Your message:")

# # Handle user's message and chatbot's response
# if user_input:
#     response = chatbot.get_response(user_input)
#     st.text_area("Chat", value=f"You: {user_input}\nBot: {response}", height=300)

# # Button for ending chat
# if st.button("End Chat"):
#     response = chatbot.get_response("bye")
#     st.text_area("Chat", value=f"Bot: {response}", height=300)
