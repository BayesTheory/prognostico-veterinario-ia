@echo off
echo Rodando api.py...
start cmd /k "uvicorn models.api:app --reload --port 8000"

timeout /t 2

echo Rodando app.py...
start cmd /k "uvicorn models.app:app --reload --port 8001"

echo Pronto! Duas janelas foram abertas com suas APIs.
pause
