# Documentação do Código - Previsão do Tempo com OpenWeatherMap

## Visão Geral
Este script realiza a consulta de previsão do tempo para uma cidade especificada pelo usuário, utilizando a API OpenWeatherMap. Ele faz uma requisição HTTP para obter os dados meteorológicos e os exibe de forma legível.

## Dependências
O script requer a biblioteca `requests` para realizar as requisições HTTP. Caso a biblioteca não esteja instalada, pode-se instalá-la com:
```sh
pip install requests
```

## Estrutura do Código
### Importação de Bibliotecas
```python
import requests
```
A biblioteca `requests` é utilizada para fazer a requisição HTTP à API do OpenWeatherMap.

### Função `get_weather`
```python
def get_weather(city, api_key):
```
Esta função recebe como parâmetros o nome da cidade (`city`) e a chave da API (`api_key`). Ela constrói a URL da requisição para a API e retorna os dados meteorológicos no formato JSON.

#### Construção da URL
```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt"
```
A URL da requisição inclui os seguintes parâmetros:
- `q={city}`: Nome da cidade a ser consultada.
- `appid={api_key}`: Chave de acesso à API.
- `units=metric`: Define a unidade de temperatura como Celsius.
- `lang=pt`: Define o idioma como português.

#### Tratamento de Erros
```python
try:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
except requests.RequestException as e:
    print("Erro ao fazer a requisição:", e)
    return None
```
Se ocorrer um erro na requisição, a exceção é capturada e uma mensagem de erro é exibida.

### Execução Principal
```python
if __name__ == "__main__":
```
Este bloco garante que o código dentro dele seja executado apenas quando o script é rodado diretamente, e não quando importado como módulo.

#### Entrada do Usuário
```python
cidade = input("Digite o nome da cidade: ")
```
Solicita ao usuário o nome da cidade para consulta.

#### Chave da API
```python
api_key = "sua_chave"
```
A chave de API é necessária para acessar os serviços da OpenWeatherMap.

#### Chamada da Função e Processamento dos Dados
```python
dados = get_weather(cidade, api_key)
```
Os dados retornados pela API são armazenados na variável `dados`.

#### Extração e Exibição dos Dados
Se a requisição for bem-sucedida (`cod == 200`), os dados são extraídos e exibidos:
```python
if dados and dados.get("cod") == 200:
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    umidade = dados["main"]["humidity"]
    velocidade_vento = dados["wind"]["speed"]

    print(f"\nPrevisão do tempo para {cidade}:")
    print(f"Temperatura: {temperatura}°C")
    print(f"Condições: {descricao.capitalize()}")
    print(f"Umidade: {umidade}%")
    print(f"Velocidade do vento: {velocidade_vento} m/s")
```
Caso ocorra um erro, a mensagem de erro fornecida pela API é exibida:
```python
else:
    mensagem = dados.get("message", "Erro desconhecido") if dados else "Sem dados"
    print(f"Não foi possível obter a previsão do tempo para {cidade}. Erro: {mensagem}")
```

## Considerações Finais
- O script é simples e eficaz para buscar informações meteorológicas.
- Para evitar o uso de uma chave de API fixa no código, pode-se utilizar variáveis de ambiente.
- O tratamento de erros poderia ser aprimorado para lidar com diferentes cenários, como conexão lenta ou cidade inexistente.
- A implementação pode ser expandida para incluir previsão para múltiplos dias ou dados adicionais como sensação térmica e pressão atmosférica.

###para saber mais sobre como usar e criar uma chave API KEY. Importante dizer que ao criar a chave pode levar um tempo até ela funcionar.
###https://www.ionos.com/pt-br/digitalguide/sites-de-internet/desenvolvimento-web/openweather-api-key/

###código
import requests

def get_weather(city, api_key):
    """
    Função para buscar os dados de previsão do tempo para a cidade informada.
    """
    # URL da API com os parâmetros: cidade, chave de API, unidades em Métrica e idioma em Português
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=pt"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceções para erros HTTP
        return response.json()
    except requests.RequestException as e:
        print("Erro ao fazer a requisição:", e)
        return None

if __name__ == "__main__":
    # Solicita o nome da cidade ao usuário
    cidade = input("Digite o nome da cidade: ")

    # Sua chave de API do OpenWeatherMap
    api_key = "sua_chave"

    dados = get_weather(cidade, api_key)

    if dados and dados.get("cod") == 200:
        # Extração dos dados desejados
        temperatura = dados["main"]["temp"]
        descricao = dados["weather"][0]["description"]
        umidade = dados["main"]["humidity"]
        velocidade_vento = dados["wind"]["speed"]

        print(f"\nPrevisão do tempo para {cidade}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Condições: {descricao.capitalize()}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do vento: {velocidade_vento} m/s")
    else:
        mensagem = dados.get("message", "Erro desconhecido") if dados else "Sem dados"
        print(f"Não foi possível obter a previsão do tempo para {cidade}. Erro: {mensagem}")




