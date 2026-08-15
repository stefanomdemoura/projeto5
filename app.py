import pandas as pd
import streamlit as st
import plotly_express as px

vehicles = pd.read_csv('vehicles.csv')


st.header('Análise de preços de veículos')
hist_button = st.button('Criar histograma de preços')
disp_button = st.button('Criar gráfico de dispersão')

if hist_button:
    fig = px.histogram(vehicles, x='price')
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    fig = px.scatter(vehicles, x='model_year', y='price',
                     color='fuel', hover_data=['model'])
    fig.update_xaxes(tickformat='d')
    st.plotly_chart(fig, use_container_width=True)
