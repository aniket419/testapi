import streamlit as st
from langchain_groq import ChatGroq

st.title('Gen ai application')
user_input = st.text_input('Enter a your query:')




submit_button = st.button("Submit")

if submit_button:
    def groq(x):
        llm = ChatGroq(temperature=0, groq_api_key='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', model_name="llama-3.1-70b-versatile")
        response = llm.invoke(user_input)
        return response.content
    st.write('Customized Message:', groq(user_input))
