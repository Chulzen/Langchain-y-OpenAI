import os
from constants import OPENAI_API_KEY
from langchain.llms import OpenAI
import streamlit as st

# Configurar la clave en el entorno (opcional)
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit framework
st.title('LangChain Demo con OpenAI API')
input_text = st.text_input('Busca el tema que quieras')

# Inicializar modelos OpenAI
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.8)

if input_text:
    st.write(llm(input_text))