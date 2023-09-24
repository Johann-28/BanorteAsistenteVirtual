import streamlit as st
import os
from page1 import page1
from page2 import page2

# Define una variable para realizar un seguimiento de la página actual
current_page = "Página 1"

# Configura la barra lateral con opciones de navegación
page_options = ["Página 1", "Página 2"]
page_selector = st.sidebar.selectbox("Navegar a:", page_options)

# Mostrar la página seleccionada
if page_selector != current_page:
    current_page = page_selector

if current_page == "Página 1":
    page1()
elif current_page == "Página 2":
    page2()


import openai

with st.sidebar:
    openai_api_key = "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"
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"


# Define el mensaje que se mostrará al principio
initial_message = "Hola, en qué puedo ayudarte hoy?"

# Define el prompt inicial para el modelo de lenguaje
initial_prompt = "Respondeme como si fueras un asesor financiero queriendome asesorarme sobre inversiones personales"

# ...

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": initial_message}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": initial_prompt + "\n" + prompt})  # Agrega "\n" para separar los mensajes
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

        
    num_tokens_used = response['usage']['total_tokens']
    st.write(f"Número de tokens utilizados: {num_tokens_used}")