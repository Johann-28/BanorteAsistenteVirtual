# Configura la página en dos columnas
import streamlit as st
import matplotlib.pyplot as plt
import openai
import plotly.express as px
from streamlit_apexjs import st_apexcharts
import numpy as np

col1, col2 = st.columns([1, 1])
def mostrar_imagen():
    url = 'banorte-logo.png'  
    st.image(url, caption='El banco de mexico')

# Define una función para mostrar el gráfico de pastel
def mostrar_grafico_pastel():
    labels = ['Gasto fijo', 'Ahorro', 'Inversion' ]
    sizes = [7500, 1500, 1000 ]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Hace que el gráfico de pastel sea un círculo.

    labels = ["Ingresos fijos", "Ahorros", "Inversiones"]

    # Muestra el gráfico en la columna 1
    with col1:
        st.plotly_chart(px.pie(names=labels, values=sizes, hole=0.3).update_traces(textinfo="percent+label"), use_container_width=True)

def mostrar_grafico_lineas():
    num_points = 20
    fig, ax = plt.subplots()

    # Genera datos para las líneas fluctuantes
    sin_invertir = np.random.uniform(2500, 2500, num_points)  # Fluctúa entre 1990 y 2010
    mejor_caso = np.random.uniform(2500, 2720, num_points)  # Fluctúa entre 2180 y 2220
    peor_caso = np.random.uniform(2550, 2400, num_points)  # Fluctúa entre 1780 y 1820

    # Agrega líneas horizont
    ax.plot(sin_invertir, linestyle='--', color='r', label="Objetivo (fluctuante)")
    ax.plot(mejor_caso, linestyle='--', color='g', label="Mejor Caso (fluctuante)")
    ax.plot(peor_caso, linestyle='--', color='b', label="Peor Caso (fluctuante)")

    # Agrega etiquetas a los ejes X e Y
    ax.set_xlabel("Horizonte de inversion/riesgo")
    ax.set_ylabel("Rendimientos")

    # Leyenda
    ax.legend()

    with col2:
        st.pyplot(fig)

def chatbot():
    
    mostrar_imagen()

    mostrar_grafico_pastel()

    mostrar_grafico_lineas()


    st.title("💬 Banorte Asistente virtual")
    st.caption("Ben")

    #Intereses

    # Mostrar la opción seleccionada por el usuario
    opcionesIntereses = ["Ahorrar para una casa", "Ahorrar para un carro", "Otras opciones"]
    intereses = st.selectbox("Selecciona tus intereses:", opcionesIntereses, key="intereses")
    if intereses == "Otras opciones":
        intereses = st.text_input("Escribe tus intereses:")

    
    # Plazos
    opcionesPlazos = ["6 meses", "1 año", "5 años o más"]
    plazo = st.selectbox("Selecciona un plazo:", opcionesPlazos, key="plazo")

    # Mostrar la opción seleccionada por el usuario 
    if plazo == "Otras opciones":
        plazo = st.text_input("Escribe tu plazo:")

    
    with col2:
        openai_api_key = "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"

    # Define el mensaje inicial de la IA
    initial_message = "Hola, en qué puedo ayudarte hoy?"
    ingreso_mensual = 10000
    gasto_promedio = 75
    edad = 19

    # Define el prompt inicial para el modelo de lenguaje
    initial_prompt = f'''

Responde como si fueras un asesor financiero queriéndome asesorar sobre inversiones personales,   Considera que tengo un ingreso mensual de ${ingreso_mensual} en los últimos 3 meses gasto un promedio de {gasto_promedio} por ciento de su sueldo así que tienes que sugerirle cuanto debería de invertir, considera que sus intereses son {intereses} y a un plazo de {plazo}, necesitas decirme si es una buena opción y guiarme a una buena inversión, eres de parte del banco Banorte así que responde como empleado de Banorte; toma en cuenta el siguiente glosario que te será de utilidad como guía.
GLOSARIO PARA INVERSIONISTAS
Estos términos te servirán para irte familiarizando con conceptos que leerás o escucharás en tu camino como inversionista.
-	Activo de renta fija: Representa parte de una deuda que Financia las operaciones de una empresa o un Estado. Se dice que es de Renta fija ya que, si mantenemos la inversión hasta el vencimiento nos dará un rendimiento que conocemos desde el principio. Por ejemplo: Bonos gubernamentales, bancarios y corporativos; pagares, etc.
-	Activo de renta variable: representa cierta participación de una empresa o sociedad, por lo que el rendimiento que se puede obtener depende de la variación del precio del activo. Por ejemplo: Acciones de empresas, derivados, títulos de fondos de inversión, etc.
CALIFICACIÓN
Nos ayudará a conocer el nivel de riesgo de un fondo y solo se otorga a los fondos de deuda. La calificación se conforma de dos partes: el riesgo del crédito y la sensibilidad de la tasa, como se muestra a continuación:
-	Para la Calificación de Riesgos de crédito: AAA es sobresaliente, AA es alto, A es Bueno, BBB es Moderado, B es Aceptable y B es Bajo.
-	Para la calificación de Sensibilidad de Tasa: 1 es Extremadamente baja, 2 es Baja, 3 es Entre baja y Moderada, 4 es Moderada, 5 es entre Moderada y Baja, 6 es Alta y 7 es Muy Alta.
DISPONIBILIDAD
Es el tiempo que transcurre desde la solicitud de compra o venta de títulos de un fondo hasta el momento en que se liquida.
HORIZONTE DE INVERSIÓN
Es el tiempo o plazo recomendado para permanecer en el fondo y así lograr optimizar los rendimientos.  Se define como Corto (en plazos de 0 a 1 año), Mediano (en plazos de 3 a 5 años) y Largo (en plazos de 5 o más años).
LIQUIDEZ: representa las inversiones que se mantienen en efectivo como los reportes o chequeras productivas.
MINUSVALÍA: es el diferencial negativo entre el precio de compra y el precio actual, se convierte en perdida solo hasta que se ejecuta la venta.
PERFIL DE INVERSIONISTA: características y/o necesidades de una persona, que determinan el rechazo o tolerancia al riesgo en sus inversiones para elegir fondos acordes a su estrategia.
PROSPECTO DE INFORMACIÓN: documento oficial en el que se describen las características de un fondo específico, así como informaciones relevantes sobre valores y estrategias. De esta manera el inversionista puede formarse una opinión más clara e informada antes de tomar una decisión de inversión. 

RENDIMIENTO: la ganancia que se obtiene al hacer efectiva la venta de los títulos del fondo. 
RIESGO: todos los fondos tienen un riesgo asociado desde extremadamente bajo hasta alto. en general, mientras mayor riesgo tiene, se espera mayor rendimiento y viceversa. 
ES EN BASE A ESTOS TERMINOS QUE SE EMPIEZA A IDENTIFICAR Y DEFINIR CUÁL ES EL PERFIL DE INVERSIONISTA DE CADA INDIVIDUO PARA COMENZAR A HACER CRECER TU DINERO. ES MUY IMPORTANTE TENER CLARO TU “PERFIL”, ES DECIR, TUS NECESIDADES E INTERESES COMO INVERSIONISTA. ALGUNOS DATOS IMPORTANTES SON: EL TIEMPO QUE DESEAS MANTENER TU DINERO INVERTIDO Y LA META QUE DESEAS ALCANZAR. AL IDENTIFICAR TUS OBJETIVOS Y SENSIBILIDAD AL RIESGO, PODREMOS BRINDARTE LAS OPCIONES EN FONDOS DE INVERSIÓN QUE SE ADAPTEN A TU PERFIL.
Además, considera los siguiente datos acerca de los fondos de inversión disponibles en Banorte; como lo siguiente (considerando las posibles respuestas a preguntas similares a las que a continuación se presentan):
¿Qué es un fondo de inversión?
Los Fondos de Inversión son una excelente forma para obtener rendimientos de tus ahorros. Su función principal es captar, invertir y administrar los recursos de clientes como tú para invertirlos en distintos instrumentos financieros y ponerlos a tu alcance. Funcionan como una sociedad que reúne el ahorro de varias personas que también buscan invertir, pero que, por los montos o instrumentos, no pueden hacerlo de manera individual.
¿Cómo puedo empezar a invertir en un Fondo?
Nuestro equipo de expertos invierte todo el tiempo en diferentes activos, según las estrategias de cada Fondo. Tú, solo tienes que elegir el o los Fondos que más te interesen. De acuerdo con tu elección irás recibiendo rendimientos, que son resultado de la rentabilidad o ganancia de los activos en los que invirtió el Fondo que elegiste.
Otra consideración importante que debes considerar son los Requisitos de contratación, que son los siguientes (y te pueden servir por si te preguntan):
Contratar tu Fondo de Inversión es muy fácil.
Solo necesitas:
-	Fondo Banorte Cete, Dólares, Dólares+, Estrategia (NTE1, NTE2, NTE3, NTED) e IPC+
-	 Tener una cuenta de débito
-	Firmar la carátula de Fondos de Inversión ya sea de forma digital (contraseña / token) o         física
¿Dónde contratar?
-	Banorte Móvil
-	Banco en Línea
-	Sucursal Banorte
Requisitos de contratación
o	Tener una cuenta de débito
o	Firmar la carátula de Fondos de Inversión ya sea de forma digital (contraseña / token) o física
Antes de invertir te recomendamos
o	Conocer cuál es tu perfil de inversionista (Preservación de Capital, Conservador, Moderado, Balanceado y Crecimiento), puedes hacerlo en cualquier sucursal
o	Conocer las características del Fondo en el que te gustaría invertir revisando el Prospecto de
Información o DICI (Documento de Información Clave para la Inversión).
(Lo anterior es aplicable para todo tipo de fondo y fondo estrategia de inversión en banorte).
Como consultor de inversiones también debes saber que Banorte ofrece diferentes tipos de fondos de inversión los cuales van a depender del tipo de inversión que el prospecto quiera realizar, a continuación, se enlistan los tipos en conjunto con sus características de cada una y los puntos importantes a analizar según los intereses del prospecto a inversionista en nuestro banco Banorte, busca recomendarle siempre la mejor opción para su porcentaje disponible para invertir: 
1.	BANORTE Cete
Fondo Banorte Cete (NTECT)
•	Fondo de deuda
o	Te permitirá obtener un rendimiento adicional a tus ahorros, sin permanencia mínima y con la liquidez inmediata que necesitas.
•	Riesgo
o	Extremadamente bajo.
•	Perfil de Inversionista
o	Dirigido a inversionistas que buscan hacer crecer sus ahorros.
o	Ideal para el perfil de Preservación de Capital que mantiene estable su capital sin correr riesgos.
•	Estrategia
o	Es un fondo 100% de deuda con un horizonte de inversión a corto plazo compuesto por valores gubernamentales y bancarios que busca obtener un rendimiento adicional a la  deuda gubernamental.
Conoce sus rendimientos históricos
a)	Serie física NTECT F7, con rango de inversión de $50 – $149,999, con comisión del 2.05%, el ultimo mes del 8.74%, en el año un 8.42% y por 12 meses un 6.99%
b)	Serie física NTECT F6, con rango de inversión de $150,000 – $299,999, con comisión del 1.80%, el último mes del 8.95%, en el año un 8.63% y por 12 meses un 7.21%
c)	Serie física NTECT F5, con rango de inversión de $300,000 – $999,999, con comisión del 1.60%, el último mes del 9.19%, en el año un 8.88% y por 12 meses un 7.47%.

d)	Serie física NTECT F4, con rango de inversión de $1,000,000 – $4,999,999, con comisión del 1.50%, el último mes del 9.35%en el año un 9.05% y por 12 meses un 7.65%.

e)	Serie física NTECT F3, con rango de inversión de $5,000,000 – $9,999,999, con comisión del 1.25%, el último mes del 9.71%, en el año un 9.41% y por 12 meses un 8.04%.

f)	Serie física NTECT F2, con rango de inversión de $10,000,000 – $49,999,999, con comisión del 1.00%, el último mes del 10.01%, en el año un 9.71% y por 12 meses un 8.35%.

g)	Serie física NTECT F1, con rango de inversión de $50,000,000 – en adelante, con comisión del 0.75%, el último mes del 10.30%, en el año un 10.01% y por 12 meses un 8.67%.


Cabe recordar que los Rendimientos netos anualizados (después de la retención de impuestos correspondientes y comisiones).
Los rendimientos pasados no garantizan rendimientos futuros.
Series Accionarias: F1, F2, F3, F4, F5, F6, F7 (Personas Físicas), Comisión por administración conforme al rango de inversión.
•	Composición de Cartera
o	Liquidez 50.69%
o	Bondes F 22.27% 
o	Revisables IPAB Mensual  
o	Bondes D 3.90%
o	Pagaré al Vencimiento 4.75%  
o	Certificados de Depósito 6.86%
o	Cert. bursátil de Banca de Desarrollo 1.30%  
o	Revisables IPAB Trimestral 0.37%
o	Cert. bursátil Bancarios 0.91%  
o	Revisables IPAB Semestral 0.30%  
o	CETES 0.01%

•	El NTECT nos brinda
o	Un horizonte de inversión: corto plazo.
o	Plazo mínimo recomendado: 1 mes.
o	Calificación: AAA/1.
o	Perfil de inversionista: Todos los perfiles.
o	Horario de operación: 8:00 a 14:30 horas
o	Disponibilidad: mismo día.
o	Inversión mínima: $50 mnx.
o	Segmento: personal y preferente. 
Fondo Banorte Digital (NTEDIG)
•	Tipo de Fondo
Fondo de Deuda.
Opera completamente en línea y por sus comisiones preferenciales te permitirá obtener un rendimiento adicional a tus ahorros, sin permanencia mínima y con la liquidez  inmediata que necesitas.
•	Riesgo
Extremadamente bajo.
•	Perfil de Inversionista
Dirigido a inversionistas que buscan hacer crecer sus ahorros de una forma totalmente digital.
Ideal para el perfil de Preservación de Capital que mantiene estable su capital sin correr riesgos.
•	Estrategia
Es un fondo 100% de deuda con un horizonte de inversión a corto plazo compuesto por valores gubernamentales y bancarios que busca obtener un rendimiento adicional a la deuda gubernamental.			
Conoce sus rendimientos históricos
a)	Serie física NTEDIG F1, con un rango de inversion de $50.00 en delante, con una comisión del 1.00%, el ultimo mes con un 10.06%, en el año con 9.76% y a 12 meses con un 8.39%.
Rendimientos netos anualizados (después de la retención de impuestos correspondientes y comisiones). Los rendimientos pasados no garantizan rendimientos futuros. Serie Accionaria: F1 (Personas Físicas), comisión por administración.  

•	Composición de Cartera
-	Liquidez 58.84%
-	Bondes F 19.05%  
-	Revisables IPAB Mensual 
-	Bondes D 3.00%
-	Cert. bursátil de Banca de Desarrollo 1.80%  
-	Pagaré al Vencimiento 3.66%
-	Cert. bursátil Bancarios 1.17%  
-	Certificados de Depósito 5.28%  
-	Revisables IPAB Trimestral 0.28%  
-	Revisables IPAB Semestral 0.23%  
-	CETES 0.01%

•	El NTEDIG nos brinda
o	Un horizonte de inversión: corto plazo.
o	Plazo mínimo recomendado: 1 mes.
o	Perfil de inversionista: Todos los perfiles.
o	Horario de operación: 8:00 a 14:30 horas
o	Disponibilidad: mismo día.
o	Inversión mínima: $50 mnx.
o	Segmento: personal y preferente.
        '''

    # Verifica si la sesión ya tiene mensajes
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": initial_message}]

    # Muestra los mensajes existentes
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # Captura la entrada del usuario
    if prompt := st.chat_input():
    
        # Configura la API de OpenAI con la clave
        openai.api_key = openai_api_key

        # Agrega el mensaje del usuario a la conversación
        st.session_state.messages.append({"role": "user", "content": initial_prompt + "\n" + prompt})
        st.chat_message("user").write(prompt)

        # Realiza una solicitud a OpenAI para obtener una respuesta
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)

        # Muestra la cantidad de tokens utilizados en la respuesta
        num_tokens_used = response['usage']['total_tokens']
        st.write(f"Número de tokens utilizados: {num_tokens_used}")


chatbot()