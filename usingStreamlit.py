import streamlit as st
from dotenv import load_dotenv
import os
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.messages.concrete.SystemMessage import SystemMessage
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.MaxSystemContextConversation import MaxSystemContextConversation

load_dotenv()
API_KEY = os.getenv("API_KEY")
llm = GroqModel(api_key=API_KEY)
allowed_models = llm.allowed_models
conversation = MaxSystemContextConversation()

def load_model(selected_model):
    return GroqModel(api_key=API_KEY, name=selected_model)

def converse(input_text, model_name):
    llm = load_model(model_name)
    agent = SimpleConversationAgent(llm=llm, conversation=conversation)


    input_text = str(input_text)

    max_retries = 3
    for attempt in range(max_retries):
        result = agent.exec(input_text)
        
        if result.strip():  # Check if the result is not blank
            return str(result)
    
    return "Sorry, I couldn't generate a response. Please try again."

st.title('My Sample bot')
st.write('Interact with the system using a selected model of your choice.')

model_name = st.selectbox("Model Name", allowed_models)
input_text = st.text_input("Input Text")

if st.button("Submit"):
    response = converse(input_text, model_name)
    st.text_area("Response", value=response, height=200)