@echo off
echo == Treinando modelos... ==
python train.py
if %ERRORLEVEL% NEQ 0 (
    echo Erro no treinamento! Abortando...
    exit /b %ERRORLEVEL%
)

echo == Iniciando a API... ==
uvicorn models.api:app --reload --port 8000
