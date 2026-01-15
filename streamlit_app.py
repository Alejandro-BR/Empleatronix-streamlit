import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

employes_df = pd.read_csv("data/employees.csv")

employes_df

st.divider()

with st.container(horizontal=True):
    color = st.color_picker("Elige un color para las barras", "#3475B3")
    names = st.toggle("Mostrar el nombre")
    salary = st.toggle("Mostrar sueldo en la barra")