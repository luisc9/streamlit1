import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import numpy as np

# data = load_iris(as_frame=True)
data = load_wine(as_frame=True)
df =data.frame

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write("Here is the wine dataframe")
st.dataframe(df)

st.write("Another change")

st.write("Let's see the description")
st.write(df.describe())


st.write("A graph")

plt.figure(figsize=(10, 6)) 
# Graficar los valores de la columna 'alcohol' 
plt.plot(df.index, df['alcohol'], marker='o', linestyle='-', color='b') 
# Añadir etiquetas y título 
plt.xlabel('Índice') 
plt.ylabel('Alcohol') 
plt.title('Valores de Alcohol en el Dataset de Vino')

st.pyplot(plt)
