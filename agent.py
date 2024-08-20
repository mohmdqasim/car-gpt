import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Car-GPT whose goal is to aid users with  car-related questions. 
        Make sure to introduce yourself in your initial message."""})
    response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Car-GPT whose goal is to aid users with  car-related questions. If a user 
        asks for information about a car, give a brief description, then list the class of car, the mechanism of action, and the efficacy presented 
        using quantitative values. Also, list the car's main competitors in point form, along with a brief description of each. Do not respond to off-topic inquiries"""})
    stream = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream