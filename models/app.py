import streamlit as st
import joblib
import numpy as np
from fastapi import FastAPI

app = FastAPI()

# Carrega modelos
modelo_desfecho = joblib.load('models/modelo_desfecho.pkl')
modelo_dias = joblib.load('models/modelo_dias.pkl')

st.title("🐶 Diagnóstico Veterinário Automatizado")

# Inputs
FC = st.number_input("Frequência Cardíaca", 0, 300, 100)
FR = st.number_input("Frequência Respiratória", 0, 100, 20)
PAS = st.number_input("Pressão Arterial Sistólica", 0, 300, 120)
Temp = st.number_input("Temperatura", 30.0, 42.0, 38.5)
Hematocrito = st.number_input("Hematócrito", 0.0, 100.0, 40.0)
# ⚠️ Adicione outros inputs conforme as features do seu modelo

# Botão de previsão
if st.button("Prever Desfecho e Dias de Internação"):
    entrada = np.array([[FC, FR, PAS, Temp, Hematocrito]])
    desfecho = modelo_desfecho.predict(entrada)[0]
    dias = modelo_dias.predict(entrada)[0]

    st.success(f"**Desfecho:** {desfecho}")
    st.info(f"**Dias estimados de internação:** {dias:.1f}")
