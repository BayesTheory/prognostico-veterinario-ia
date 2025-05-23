import requests

def testar_api():
    url = "http://127.0.0.1:8000/prever"
    
    payload = {
        "FC": 80.0,
        "FR": 20.0,
        "PAS": 120.0,
        "Temp": 38.5,
        "Hematocrito": 45.0
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Gera exceção se status != 200
        
        print("✅ Sucesso!")
        print("Resposta:", response.json())
        
    except requests.exceptions.HTTPError as errh:
        print("❌ Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("❌ Erro de Conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("❌ Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("❌ Erro:", err)

if __name__ == "__main__":
    testar_api()

