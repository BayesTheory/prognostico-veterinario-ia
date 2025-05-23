from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os

app = FastAPI()

# === Carregar modelos e label encoders ===
modelo_desfecho = joblib.load(os.path.join('models', 'modelo_desfecho.pkl'))
modelo_dias = joblib.load(os.path.join('models', 'modelo_dias.pkl'))
le_y = joblib.load(os.path.join('models', 'label_encoder_y.pkl'))
features_treinadas = joblib.load(os.path.join('models', 'features.pkl'))  # ✅ Carregando as features

class DadosEntrada(BaseModel):
    FC: float
    FR: float
    PAS: float
    Temp: float
    Hematocrito: float

@app.post("/prever")
def prever(dados: DadosEntrada):
    # ✅ Criar DataFrame de entrada
    entrada = pd.DataFrame([{
        "FC": dados.FC,
        "FR": dados.FR,
        "PAS": dados.PAS,
        "Temp": dados.Temp,
        "Hematocrito": dados.Hematocrito
    }])

    # ✅ Garantir que todas as features estejam presentes
    for col in features_treinadas:
        if col not in entrada.columns:
            entrada[col] = 0  # ou np.nan, dependendo do tratamento

    # ✅ Garantir mesma ordem
    entrada = entrada[features_treinadas]

    # === Previsões ===
    desfecho_codificado = modelo_desfecho.predict(entrada)[0]
    desfecho = le_y.inverse_transform([desfecho_codificado])[0]

    dias_internacao = modelo_dias.predict(entrada)[0]

    return {
        "desfecho_previsto": desfecho,
        "dias_previstos_internacao": dias_internacao
    }
