import pandas as pd
import streamlit as st

st.title('WalMart USA App')

DATA_URL = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'

@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

def filter_data(df, column, option):
    df = df.loc[df[column] == option]
    return df

data = load_data()

st.header('Filtro')
st.write('Mostrar información de la base de datos de WalMart USA filtrando el modo de envío, la categoría y el descuento de las órdenes.')

ship_mode = st.radio('Control Ship Mode', data['Ship Mode'].unique())
df = filter_data(data, 'Ship Mode', ship_mode)

category = st.selectbox('Control Category', data['Category'].unique())
df = filter_data(df, 'Category', category)

discount = st.slider('Control Discount', data['Discount'].min(), data['Discount'].max())
df = filter_data(df, 'Discount', discount)

st.dataframe(df)