from transformers import pipeline

# Load free LLM from Hugging Face (you can choose others too)
llm = pipeline("text-generation", model="openchat/openchat-3.5", max_new_tokens=256)

# Function to query the LLM
def ask_llm(prompt: str) -> str:
    response = llm(prompt)[0]['generated_text']
    return response.replace(prompt, "").strip()

# Start conversation

def start_session(name: str):
    prompt = f"""
You are a mental health assistant in a hospital. Begin a friendly conversation with a patient named {name}.
Start with a welcoming message, ask how they're doing today, and begin a PHQ-9 style depression screening.
Ask questions one at a time, wait for patient responses.
"""
    return ask_llm(prompt)

# Continue conversation based on user input
def follow_up_prompt(user_response: str):
    prompt = f"""
The patient responded: \"{user_response}\".
Based on this, ask the next screening question related to depression or mood.
Keep it conversational and empathetic.
"""
    return ask_llm(prompt)

# Emotion Detection
def detect_emotion(user_input: str):
    prompt = f"""
You're a clinical psychologist. Analyze the emotional tone of this sentence and label it as one of the following:
[Happy, Sad, Anxious, Hopeless, Energetic, Neutral]

Sentence: \"{user_input}\"

Reply with just the emotion label.
"""
    return ask_llm(prompt)

# LLM-based scoring of user's answer
def score_user_response(response: str):
    prompt = f"""
You are a licensed psychiatrist. Based on this patient's answer:
\"{response}\"

1. Rate the emotional distress from 0 to 3 based on PHQ-9 scale:
   - 0 = Not at all
   - 1 = Several days
   - 2 = More than half the days
   - 3 = Nearly every day

2. Explain your reasoning briefly.

Format:
Score: [number]
Reason: [your explanation]
"""
    return ask_llm(prompt)
