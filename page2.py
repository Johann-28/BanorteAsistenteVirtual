import streamlit as st
import matplotlib.pyplot as plt

def page2():
    st.title("Página 2")
    st.write("Este es el contenido de la página 2.")
    
    labels = ['Manzanas', 'Plátanos', 'Naranjas', 'Uvas']
    sizes = [30, 25, 15, 30]

    # Crear un gráfico de pastel
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Hace que el gráfico de pastel sea un círculo.

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    if st.button("Ir a la Página 1"):
        return "Página 1"  # Devuelve el nombre de la página a la que se debe navegar
