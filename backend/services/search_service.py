import requests
import os
from dotenv import load_dotenv

load_dotenv()

SEMANTIC_SCHOLAR_URL = f"https://www.semanticscholar.org/search"
HEADERS = {"User-Agent": "TCC_UNIPENSE_AI"}

def search_semantic_scholar(query: str, limit: int = 5):
    """Busca artigos acadêmicos no Semantic Scholar"""
    params = {"query": query, "limit": limit}
    response = requests.get(SEMANTIC_SCHOLAR_URL, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        return response.json()
    return {"error": "Falha na requisição", "status": response.status_code}

