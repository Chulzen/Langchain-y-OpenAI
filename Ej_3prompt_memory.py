#ahora lo modificamos para poder hacerlo con nuestras propiar prmpts con simple chain

import os
from constants import OPENAI_API_KEY
from langchain.llms import OpenAI
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory

from langchain.chains import SequentialChain

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

nombre_memory = ConversationBufferMemory(input_key='nombre', memory_key='chat_history')

chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key= 'descripcion',memory=nombre_memory)


#Prompt Templates
second_input_prompt = PromptTemplate(
    input_variables = ['dscripcion'],
    template = "Dame el Precio espefefico de {descripcion} en el mercado chino"
    )

descripcion_memory = ConversationBufferMemory(input_key='descripcion', memory_key='chat_history')
chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key= 'precio en dolares',memory=descripcion_memory)
#Prompt Templates
third_input_prompt = PromptTemplate(
    input_variables = ['precio en dolares'],
    template = "Entregame en una lista de puntos, 5 elementos que tengan el mismo {precio en dolares} que la fruta"
    )
precio_memory = ConversationBufferMemory(input_key='precio en dolares', memory_key='description_history')
chain3=LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key= 'lista',memory=precio_memory)

parent_chain = SequentialChain(chains=[chain,chain2,chain3],input_variables=['nombre'],output_variables=['descripcion','precio en dolares','lista'],verbose=True)


if input_text:
    st.write(parent_chain({'nombre':input_text}))

    with st.expander('Nombre fruta'):
        st.info(nombre_memory.buffer)

    with st.expander('Descripcion Fruta'):
        st.info(descripcion_memory.buffer)

    with st.expander('Precio fruta'):
        st.info(precio_memory.buffer)