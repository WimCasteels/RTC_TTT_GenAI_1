import streamlit as st
from chatbot_functies import chatbot_response


st.title("🤖 Learning AI 🤖")
st.markdown("Software applicaties met generatieve AI: masterclass 2")
form = st.form(key="user_settings")
with form:
    AI_concept = st.text_input("Enter the AI concept you are interested in:", key = "AI_concept")
    role = st.selectbox("For what audience would you like it to be explained?",
                          ("Expert", 
                           "Layman", "12 year old child"),)
    generate_button = form.form_submit_button("Explain AI concept")
    if generate_button:
        with st.spinner('Wait for it...'): #add a waiting icon while waiting for the response
            PROMPT = f"""Concisely explain the AI concept {AI_concept} to someone with the experience of a {role} in the field of artificial intelligence. 
            Do not give an answer if the concept is not related to AI."""
            response = chatbot_response(PROMPT)
        st.write(response)
