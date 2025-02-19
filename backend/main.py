from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bem-vindo à API do TCC_UNIPENSE_AI!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/search")
def search(query: str):
    # Lógica para buscar nas APIs acadêmicas
    return {"query": query, "results": []}  # Placeholder

# Rota para documentação automática do Swagger
@app.get("/docs")
def documentation():
    return {"message": "Acesse /docs no navegador para ver a documentação."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
