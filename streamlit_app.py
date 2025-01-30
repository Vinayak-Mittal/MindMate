import streamlit as st
import ollama
import base64
import os

st.set_page_config(page_title="Mental Health Chatbot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_base64(background):
    if not os.path.exists(background):
        st.error(f"Error: {background} not found. Ensure the file is uploaded correctly.")
        return ""  # Return an empty string if the file is missing

    with open(background, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str = get_base64("background.png")
st.write(f"Background image encoded length: {len(bin_str)}")



st.markdown(f"""
        <style>
            .main{{
            background-image:url("data:image/png;base64,{bin_str}");
            background-style: cover;
            background-position: center;
            background-repeat:no-repeat;

            }}
        </style>
        """,unsafe_allow_html=True)


st.session_state.setdefault('conversation_history',[])

def generate_response(user_input):
    st.session_state['conversation_history'].append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Change to "gpt-3.5-turbo" if needed
        messages=st.session_state['conversation_history']
    )
    
    ai_response = response["choices"][0]["message"]["content"]
    st.session_state['conversation_history'].append({"role": "assistant", "content": ai_response})
    return ai_response

def generate_affirmation():
    prompt = "Provide a positive affirmation to encourage someone who is feeling stressed or overwhelmed"
    response = ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

def generate_meditation_guide():
    prompt = "Provide a 5-minute guided meditation script to help someone relax and reduce stress."
    response=ollama.chat(model="llama3.1:8b", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

st.title("Mental Health Support Agent")

for msg in st.session_state['conversation_history']:
    role= "You" if msg['role'] == "user" else "AI"
    st.markdown(f"**{role}:** {msg['content']}")

user_message = st.text_input("How can I help you today?")

if user_message:
    with st.spinner("Thinking....."):
        ai_response = generate_response(user_message)
        st.markdown(f"**AI:** {ai_response}")

col1 , col2 = st.columns(2)

with col1:
    if st.button("Give me a positive Afiirmation"):
        affirmation = generate_affirmation()
        st.markdown(f"**Affirmation:** {affirmation}")

with col2:
    if st.button("Give me a guided meditation"):
        meditation_guide = generate_meditation_guide()
        st.markdown(f"**Guided Meditation:** {meditation_guide}")       
