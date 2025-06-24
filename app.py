import gradio as gr
from llm_agent import start_session, follow_up_prompt, detect_emotion, score_user_response

# Initialize conversation
session_started = False
chat_history = []

# Function to handle chat
def chat_interface(user_input, history):
    global session_started
    if not history:
        history = []
    
    if not session_started:
        welcome_msg = start_session("Patient")
        session_started = True
        history.append(("", welcome_msg))
        return history, history

    # Emotion detection and scoring
    emotion = detect_emotion(user_input)
    score = score_user_response(user_input)
    
    # Generate next response
    reply = follow_up_prompt(user_input)
    ai_reply = f"{reply}\n\n🔍 Emotion: {emotion}\n🧠 Score: {score}"
    history.append((user_input, ai_reply))
    return history, history

# Build Gradio UI
def build_interface():
    with gr.Blocks() as demo:
        gr.Markdown("## 🧠 AI-Powered Psychometric Chat Assessment")
        chatbot = gr.Chatbot()
        user_input = gr.Textbox(label="Your response")
        state = gr.State([])

        user_input.submit(chat_interface, [user_input, state], [chatbot, state])
        user_input.submit(lambda: "", None, user_input)

    return demo

if __name__ == "__main__":
    demo = build_interface()
    demo.launch()
