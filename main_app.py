import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime as dt

df = pd.read_csv('https://raw.githubusercontent.com/jesusjfy/QAIRA/main/13_Monitoreo_Junio_2021.csv',sep=";")

df.columns = ['Id','Codigo_entidad','Codigo_ubigeo','Codigo_pais','Nombre_uo','Fecha','CO','H2S','NO2','O3','PM10', 'PM25', 'SO2',
       'Ruido', 'UV', 'Humedad', 'Latitud', 'Longitud','Presion', 'Temperatura

df['Fecha'] = pd.to_datetime(df['Fecha'])
df = df.sort_values('Fecha')

#df['Fecha_datetime'] = pd.to_datetime(df['Fecha'])
#df['Dia'] = df['Fecha_datetime'].dt.day
#df['Mes'] = df['Fecha_datetime'].dt.month
#df['Anio'] = df['Fecha_datetime'].dt.year
#df['Tiempo'] = df['Fecha_datetime'].dt.time

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('./style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard')
st.sidebar.subheader('Parámetros')
parametros_linea = st.sidebar.selectbox('Selecciona una opción', ('CO','H2S','NO2','O3','PM10', 'PM25', 'SO2',
       'Ruido', 'UV', 'Humedad','Presion', 'Temperatura'))

st.markdown('### Promedios')
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", str("{:.2f}".format(df['Temperatura'].mean()) + " °C"), str("{:.2f}".format(20 - df['Temperatura'].mean()) + " °C"))
col2.metric("Presión", str("{:.2f}".format(df['Presion'].mean()) + " Pa"), str("{:.2f}".format(1000 - df['Presion'].mean()) + " Pa"))
col3.metric("Humedad", str("{:.2f}".format(df['Humedad'].mean()) + " %"), str("{:.2f}".format(100.00 - df['Humedad'].mean()) + " %"))

st.markdown('### Gráfico de línea')
st.line_chart(df, x = 'Fecha', y = parametros_linea, height = 500)
