import streamlit as st
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

api = os.getenv('GOOGLE_API_KEY')

i = 0
def talk():
        user_input = st.text_input('Talk with DataFrame...', key=f"input_{i}") # pass a unique key argument
        if st.button('Execute', key=f"button_{i}"): # also pass a unique key argument to st.button
            with st.spinner('Thinking...'):
                st.info(agent.run(user_input))
            


llm = GoogleGenerativeAI(
    model="gemini-pro", google_api_key=api)


st.title('Pandas Ai 🐼')

csv = st.file_uploader('Upload your csv file', type=('csv', 'txt'))
btn = None
if csv is not None:
    df = pd.read_csv(csv)
    st.dataframe(df.head(5))
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    #input = st.text_input('Talk with DataFrame...')
    #btn = st.button('Execute')

    talk()
# if btn:
#     with st.spinner('Thinking...'):
#         # I added a try-except block to handle possible errors
#         try:
#             st.info(agent.run(input))
#             talk()
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
