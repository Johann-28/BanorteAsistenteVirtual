import streamlit as st

def page1():
    st.write("""
    # My first app
    Hello *world!*
    """)
    
    number = st.slider("Pick a number", 0, 100)
    st.title("Página 1")
    st.write("Este es el contenido de la página 1.")
    if st.button("Ir a la Página 2"):
        return "Página 2"  # Devuelve el nombre de la página a la que se debe navegar
