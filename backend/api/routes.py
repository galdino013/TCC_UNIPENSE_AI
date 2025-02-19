from fastapi import APIRouter, Query
from services.search_service import search_semantic_scholar

router = APIRouter()

@router.get("/search/semantic-scholar")
async def search_scholar(query: str = Query(..., min_length=3), limit: int = 5):
    """Rota para buscar artigos no Semantic Scholar"""
    return search_semantic_scholar(query, limit)

@app.route('/search', methods=['GET'])
def search_articles():
    # Parâmetros da requisição, que podem ser passados pela query string da URL
    query = request.args.get('q', 'machine learning')  # Palavra-chave de pesquisa
    page = request.args.get('page', 1)                 # Página de resultados
    size = request.args.get('size', 10)                # Número de resultados por página
    
    # Definindo parâmetros da requisição
    params = {
        'q': query,
        'page': page,
        'size': size
    }

    # Cabeçalhos com a chave da API
    headers = {
        'Authorization': f'Bearer {yakT8IHXLO0u1B453spirzDqCelSAngF}'
    }

    # Realizando a requisição à CORE API
    response = requests.get(base_url, params=params, headers=headers)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        # Retornando os artigos encontrados como resposta JSON
        return jsonify(data['data'])
    else:
        return jsonify({"error": "Erro ao buscar artigos", "status_code": response.status_code}), 500