import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("ESTADISTICA DE SALAS ")

st.image("imagen/sala5.jpg", width=600)

ruta_imagen = "imagen/Logo_ctecnoazul.jpg"
ancho_deseado = 200

centrado_css = """
    <style>
    .image-container {
        display: flex;
        justify-content: center;
       
    }
    </style>
"""
st.markdown(centrado_css, unsafe_allow_html=True)


st.sidebar.image(ruta_imagen, width=ancho_deseado)

df = pd.read_csv('static\datasets\Salas2 (1).csv', parse_dates=['HORA'])

DIA = st.multiselect('DIA', sorted(set(df['DIA'].unique())))
HORA = st.multiselect('HORA', sorted(set(df['HORA'].dt.strftime('%H:%M').unique())))

df_filtrado = df[df['DIA'].isin(DIA) & df['HORA'].dt.strftime('%H:%M').isin(HORA)]

# Crea un gráfico  
if not df_filtrado.empty:  

    filtro=df_filtrado.groupby(["SALA", "HORA"])['SALA'].count().reset_index(name='TOTAL_SALA')
    st.write(filtro)

    plt.plot(filtro['SALA'], filtro['TOTAL_SALA'])
    plt.xlabel("Eje SALA")
    plt.ylabel("Eje TOTAL")  
 
    st.pyplot(plt)
else:
    st.write("No hay datos disponibles para los filtros seleccionados.")
#-----------------------------------------------------------------------------------

#Filtro 2 