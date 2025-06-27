import urllib.request
import json

# Chave da API
API_KEY = "ef481c7b4f97d64488f89435bcd1aeb0"

def get_weather(city, state, country):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Monta a busca incluindo cidade, estado e país
    query = f"{city},{state},{country}"
    url = f"{base_url}?q={query}&appid={API_KEY}&units=metric&lang=pt"
    print(url)
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        
        if response.status == 200:
            cidade = data["name"]
            temperatura = data["main"]["temp"]
            descricao = data["weather"][0]["description"]
            umidade = data["main"]["humidity"]
            vento = data["wind"]["speed"]
            pais = data["sys"]["country"]

            print(f"\n📍 Cidade: {cidade}, {state}, {pais}")
            print(f"🌡️ Temperatura: {temperatura}°C")
            print(f"🌤️ Descrição: {descricao.capitalize()}")
            print(f"💧 Umidade: {umidade}%")
            print(f"💨 Velocidade do vento: {vento} m/s\n")
        else:
            print(f"Erro: {data.get('message', 'Não foi possível obter os dados do clima.')}")
    
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")

def main():
    cidade = input("Digite o nome da cidade: ")
    estado = input("Digite a sigla do estado: ")
    pais = input("Digite o código do país (ex: BR para Brasil): ").upper()
    
    get_weather(cidade, estado, pais)

if __name__ == "__main__":
    main()
