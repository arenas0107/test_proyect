import pandas as pd
import plotly.express as px
import streamlit as st 

# Leer los datos una sola vez
car_data = pd.read_csv('vehicles_us.csv')

st.header('Gráficos')

# Botón para el histograma
hist_button = st.button('Histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para el gráfico de dispersión
disp_button = st.button('Gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión
    fig_disp = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_disp, use_container_width=True)
