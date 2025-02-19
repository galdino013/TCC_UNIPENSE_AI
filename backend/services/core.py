import requests

# Sua chave da API da CORE
api_key = 'yakT8IHXLO0u1B453spirzDqCelSAngF'

# URL base da CORE API para buscar artigos
base_url = 'https://api.core.ac.uk/v3/articles'

# Parâmetros da requisição (exemplo: busca por 'machine learning')
params = {
    'q': 'machine learning',  # Termo de pesquisa
    'page': 1,                # Página de resultados
    'size': 10                # Número de resultados por página
}

# Cabeçalhos com a chave da API
headers = {
    'Authorization': f'Bearer {api_key}'
}

# Realizando a requisição
response = requests.get(base_url, params=params, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    data = response.json()
    print("Artigos encontrados:")
    for article in data['data']:
        print(f"Titulo: {article['title']}")
        print(f"DOI: {article['doi']}")
        print(f"Link: {article['url']}")
        print("-" * 50)
else:
    print(f"Erro: {response.status_code}")
