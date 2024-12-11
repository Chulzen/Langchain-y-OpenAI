#ahora lo modificamos para poder hacerlo con nuestras propiar prmpts con simple chain

import os
from constants import OPENAI_API_KEY
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.chains import SimpleSequentialChain

# Configurar la clave en el entorno (opcional)
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Streamlit framework
st.title('Buscador de Frutas y caracteristicas')
input_text = st.text_input('Busca la Fruta que quieras')

# Inicializar modelos OpenAI
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.8)

#Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables = ['nombre'],
    template = "Cuentanme sobre fruta {nombre}"
    )

chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key= 'nombre')

#Prompt Templates
second_input_prompt = PromptTemplate(
    input_variables = ['nombre'],
    template = "Dame el Precio espefefico de {nombre} en el mercado chinio"
    )

chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key= 'precio')

parent_chain = SimpleSequentialChain(chains=[chain,chain2],verbose=True)


if input_text:
    st.write(parent_chain.run(input_text))