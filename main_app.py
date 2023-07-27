import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime as dt

df = pd.read_csv('https://raw.githubusercontent.com/jesusjfy/QAIRA/main/13_Monitoreo_Junio_2021.csv',sep=";")

df.columns = ['Id','Codigo_entidad','Codigo_ubigeo','Codigo_pais','Nombre_uo','Fecha','CO','H2S','NO2','O3','PM10', 'PM25', 'SO2',
       'Ruido', 'UV', 'Humedad', 'Latitud', 'Longitud','Presion', 'Temperatura']


