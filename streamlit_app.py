import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

employes_df = pd.read_csv("data/employees.csv")

employes_df

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker("Elige un color para las barras", "#3475B3")

with col2:
    names = st.toggle("Mostrar el nombre")

with col3:
    salarys = st.toggle("Mostrar sueldo en la barra")


y_pos = range(len(employes_df))

fig, ax = plt.subplots()

bars = ax.barh(
    y_pos,
    employes_df["salary"],
    color=color
)

if salarys:
    for i, salary in enumerate(employes_df["salary"]):
        ax.text( salary + 20, i, f"{salary} €", va="center", color="black")

if names:
    ax.set_yticks(y_pos)
    ax.set_yticklabels(employes_df["full name"])
else:
    ax.set_yticks([])

ax.set_xlim(0, 4500)

st.pyplot(fig)

st.write("© Alejandro Barrionuevo Rosado - CPIFP Alan Turing")