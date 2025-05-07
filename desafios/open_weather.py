import urllib.request  # Importa a biblioteca padrão para requisições HTTP
import json  # Importa a biblioteca para trabalhar com JSON

# Carrega a chave da API de um arquivo .env (substitua pela sua chave real)
API_KEY = "SUA_API_KEY"

# Função para buscar os dados do clima na API do OpenWeather
def pegar_clima(cidade, estado, pais):
    base_url = "https://api.openweathermap.org/data/2.5/weather"  # URL da API
    
    # Monta a string de consulta que inclui cidade, estado e país
    query = f"{cidade},{estado},{pais}"
    
    # Monta a URL com os parâmetros necessários para a requisição
    url = f"{base_url}?q={query}&appid={API_KEY}&units=metric&lang=pt"
    # Se mandar printar essa URL e colar no navegador vai ver a magia acontecer
    
    try:
        # Faz a requisição GET para a API e lê a resposta
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())  # Converte a resposta JSON em um dicionário
        
        # Verifica se a requisição foi bem-sucedida (código 200)
        if response.status == 200:
            cidade = data["name"]  # Obtém o nome da cidade
            temperatura = data["main"]["temp"]  # Obtém a temperatura atual
            descricao = data["weather"][0]["description"]  # Obtém a descrição do clima
            umidade = data["main"]["humidity"]  # Obtém a umidade relativa do ar
            vento = data["wind"]["speed"]  # Obtém a velocidade do vento
            pais = data["sys"]["country"]  # Obtém o código do país

            # Exibe os dados formatados para o usuário
            print(f"\n📍 Cidade: {cidade}, {estado}, {pais}")
            print(f"🌡️ Temperatura: {temperatura}°C")
            print(f"🌤️ Descrição: {descricao.capitalize()}")
            print(f"💧 Umidade: {umidade}%")
            print(f"💨 Velocidade do vento: {vento} m/s\n")
        else:
            # Caso ocorra um erro na API, exibe a mensagem de erro
            print(f"Erro: {data.get('message', 'Não foi possível obter os dados do clima.')}")
    
    # Captura qualquer erro inesperado que possa ocorrer
    except Exception as e:
        print(f"Erro ao acessar a API: {e}")

# Declara a função principal do código
def main():
    # Solicita ao usuário o nome da cidade
    cidade = input("Digite o nome da cidade: ")
    
    # Solicita ao usuário a sigla do estado (opcional, dependendo do país)
    estado = input("Digite a sigla do estado: ")
    
    # Solicita ao usuário o código do país (exemplo: BR para Brasil, US para Estados Unidos)
    pais = input("Digite o código do país: ").upper()
    
    # Chama a função para pegar o clima, passando os dados coletados como parâmetros
    pegar_clima(cidade, estado, pais)

# Nomeia o código como "main", garantindo que a função main() só seja executada 
# se o arquivo for rodado diretamente e não quando for importado como módulo
if __name__ == "__main__":
    main()
