import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import streamlit as st

st.title("ESTADISTICA DE COMPUTADORES ")
st.image("imagen/HPmesa.webp", width=600)

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



df = pd.read_csv('static/datasets/compudata22.csv', parse_dates=['HORA'])


DIA = st.multiselect('DIA', sorted(df['DIA'].unique()))
HORA = st.multiselect('HORA', sorted(df['HORA'].dt.strftime('%H:%M').unique()))

MARCA = st.multiselect('MARCA', sorted(df['MARCA'].unique())) 

CODIGO = st.multiselect('CODIGO', sorted (df['CODIGO'].unique()))

df_filtro_marca = df[df['MARCA'].isin(MARCA)] 

df_filtrado_codigo = df[df['CODIGO'].isin(CODIGO)]

df_filtrado = df[df['DIA'].isin(DIA) & df['HORA'].dt.strftime('%H:%M').isin(HORA)]

# Crea un gráfico  
if not df_filtrado.empty:  
         

    filtro=df_filtrado.groupby(["MARCA", "HORA"])['MARCA'].count().reset_index(name='TOTAL_MARCA')
    st.write(filtro)

    plt.plot(filtro['MARCA'], filtro['TOTAL_MARCA'])
    plt.xlabel("Eje MARCAS")
    plt.ylabel("Eje TOTAL")  
 
 # Muestra el gráfico en Streamlit
    st.pyplot(plt)
    

if not df_filtro_marca.empty:  

    # MARCA = df_filtrado['MARCA'].tolist()
    # HORA = df_filtrado['HORA'].dt.strftime('%H:%M').tolist()

    filtro=df_filtro_marca.groupby(["MARCA", "DIA"])['DIA'].count().reset_index(name='TOTAL_POR_DIA')
    st.write(filtro)

    plt.plot(filtro['DIA'], filtro['TOTAL_POR_DIA'])
    plt.xlabel("Eje DIAS")
    plt.ylabel("Eje NUMERO RESERVAS")  
 
 # Muestra el gráfico en Streamlit
    st.pyplot(plt)
if not df_filtrado_codigo.empty:
    filtro=df_filtrado_codigo.groupby(["CODIGO", "DIA", "MARCA"])['DIA'].count().reset_index(name='TOTAL_POR_DIA')
    st.write(filtro)

    plt.plot(filtro['DIA'], filtro['TOTAL_POR_DIA'])
    plt.xlabel("Eje DIAS")
    plt.ylabel("Eje NUMERO RESERVAS")  
    
    st.pyplot(plt)
 
else:
    st.write("No hay datos disponibles para los filtros seleccionados.")


