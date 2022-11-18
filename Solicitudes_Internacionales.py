import plotly.express as px
import streamlit as st
import pandas as pd

DATA_URL1 = 'Solicitudes_Aceptadas_Final.csv'
DATA_URL2 = 'Comparacion_Solicitudes.csv'

df = pd.read_csv(DATA_URL1)
df_comp = pd.read_csv(DATA_URL2)

st.title('Análisis de Solicitudes Internacionales del Tec de Monterrey')
st.header('Análisis de oportunidades')
lra_or_tipo  = st.selectbox('¿Qué análisis desea hacer?', ['¿Fue la primera opción seleccionada respetada?', '¿Se está perdiendo dinero al enviar estudiantes?'], 0)

if lra_or_tipo == '¿Fue la primera opción seleccionada respetada?':
    data = '1raOpciónAsignada'
    hover = ['Count1raOpción']
    fig1 = px.pie(df, names=data, hover_data=hover, color_discrete_sequence=px.colors.qualitative.Prism, title=lra_or_tipo)
    st.write(fig1)
    st.write('Sí se respetan las primeras opciones seleccionadas la gran mayoría de las veces.')
else:
    data = 'TipoOportunidad'
    hover = ['CountTipoOportunidad']
    fig1 = px.pie(df, names=data, hover_data=hover, color_discrete_sequence=px.colors.qualitative.Prism_r, title=lra_or_tipo)
    st.write(fig1)
    st.write('Se pierde dinero porque hay una cantidad mucho más grade de Studies Abroad que Intercambios, causando que no tengan apoyo económico.')

st.header('Análisis de promedio necesario para ser admitido')
box_hist = st.selectbox('¿Con qué tipo de gráfico lo desea visualizar?', ['Boxplot', 'Histograma'], 0)
if box_hist == 'Boxplot':
    fig2 = px.box(df_comp, y="Promedio", color='Rechazado', color_discrete_sequence=px.colors.qualitative.Dark24_r, title='Boxplot de promedio de alumnos aceptados y rechazados')
else:
    bins = st.slider('Seleccione el número de intervalos', 10, 200, 50)
    fig2 = px.histogram(df_comp, x="Promedio", color='Rechazado', color_discrete_sequence=px.colors.qualitative.Dark24_r, nbins=bins, title='Boxplot de promedio de alumnos aceptados y rechazados')

st.write(fig2)
st.write('Aunque se observa que los admitidos sí tienen una mediana más alta que los rechazados, hay admitidos con promedios más bajos y rechazados con promedios altos.')

st.header('Visualización de procedencia y destino de los estudiantes internacionales')
colour_ = st.selectbox('Código de colores', ['Área Académica', 'Región', 'Continente del Programa'], 2)
if colour_ == 'Área Académica':
    colour = 'ColorArea'
elif colour_ == 'Región':
    colour = 'ColorReg'
else:
    colour = 'ColorCont'
fig3 = px.parallel_categories(df, dimensions=['Area Academica', 'Region', 'ContinenteDestino'], color=colour, color_continuous_scale=px.colors.sequential.Bluered_r, labels={'Area Academica':'Área Académica', 'Region':'Campus','ContinenteDestino':'Continente del Programa'})
st.write(fig3)
st.write('Las ingenierías y negocios son los más comunes para hacer estudios internacionales. Todas las regiones presentan ofrecer muchas oportunidades. Europa es por un gran margen la región más visitada en estas oportunidades, con Norteamérica siendo el segundo y Asia siendo el continente menos visitado.')

st.header('Mapa de cantidad de estudaintes con oportunidad internacional por campus')
fig4 = px.scatter_mapbox(df, lat='Latitud', lon='Longitud', hover_name='Campus', size='CountCampus', color='CountCampus', color_continuous_scale=px.colors.sequential.Bluered_r).update_layout(mapbox={"style": "carto-positron", "zoom": 4}, margin={"t":0,"b":0,"l":0,"r":0})
st.write(fig4)
st.write('En el campus de Monterrey es en donde se encuentra la mayor cantidad de oportunidades por un gran margen, seguidos por Guadalajara y Querétaro. Puede deberse a la cantidad de estudiantes por campus, pero el resto envía una cantidad de alumnos de menos del 10% que el campus Monterrey.')