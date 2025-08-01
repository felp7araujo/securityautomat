# security_api.py

import requests

# Chave de API Asaas
API_KEY = "$aact_hmlg_000MzkwODA2MWY2OGM3MWRlMDU2NWM3MzJlNzZmNGZhZGY6OmVmNWQ2YzRhLTQwMDktNGE4Yi04MTY1LTA4NmJlYjBhMGFkMjo6JGFhY2hfMDdhYjdiODgtOTExMC00MzNkLTkxZWItNmM4ZTMxMjc4ZmVm"

def chamada_exemplo():
    url = "https://api.exemplo.com/dados"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    # Simula uma chamada à API
    response = requests.get(url, headers=headers)
    
    print("Status:", response.status_code)
    print("Resposta:", response.text)

if __name__ == "__main__":
    chamada_exemplo()
