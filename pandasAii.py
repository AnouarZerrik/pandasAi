import streamlit as st
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
import random
import time
load_dotenv()

api = os.getenv('GOOGLE_API_KEY')


llm = GoogleGenerativeAI(
    model="gemini-pro", google_api_key=api)

def talk(df):
    global llm
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    result = ''
    for i in range(4):
        result += random.choice('1234567890')
        
    user_input = st.text_input('Talk with DataFrame...')
    btn = st.button('Execute')
    if btn:
        with st.spinner('Thinking...'):
            st.info(agent.run(user_input))





st.title('Pandas Ai 🐼')

csv = st.file_uploader('Upload your csv file', type=('csv', 'txt'))
if csv is not None:
    df = pd.read_csv(csv)
    st.dataframe(df.head(5))
    #user_input = st.text_input('Talk with DataFrame...')
    talk(df=df)