import streamlit as st
from llm_agent import start_session, follow_up_prompt, detect_emotion, score_user_response
from report import generate_pdf

st.set_page_config(page_title="AI Psychometric Test", page_icon="🧠")
st.title("🧠 AI-Powered Psychometric Assessment")
st.markdown("This assistant helps conduct a **PHQ-9-like depression test** using a conversational AI agent.")

# Input: Name
name = st.text_input("Enter your name")
start_button = st.button("Start Session")

if start_button and name:
    st.session_state['chat'] = [("ai", start_session(name))]

if 'chat' in st.session_state:
    for role, message in st.session_state.chat:
        st.chat_message("Assistant" if role == "ai" else "You").write(message)

    user_input = st.chat_input("Your response")
    if user_input:
        st.session_state.chat.append(("user", user_input))

        # Emotion detection
        emotion = detect_emotion(user_input)
        st.info(f"🔍 Detected Emotion: {emotion}")

        # Score response
        score_result = score_user_response(user_input)
        st.warning(f"🧠 Score Analysis:\n\n{score_result}")

        # Generate next message
        next_msg = follow_up_prompt(user_input)
        st.session_state.chat.append(("ai", next_msg))
        st.rerun()

    if st.button("📝 Generate Report"):
        conversation = [(r, m) for r, m in st.session_state.chat]
        pdf = generate_pdf(name, conversation)
        with open(pdf, "rb") as f:
            st.download_button("Download PDF Report", f, file_name=pdf)
