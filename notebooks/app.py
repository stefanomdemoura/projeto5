import pandas as pd
import streamlit as st
import plotly_express as px

vehicles = pd.read_csv('vehicles.csv')

st.header('Análise de anúncios de veículos')
hist_button = st.button('Criar gráfico')
