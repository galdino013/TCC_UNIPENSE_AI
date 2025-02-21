import React from 'react';
import './App.css';

function App() {
  // Função de redirecionamento para os endpoints
  const openGoogleScholar = () => {
    window.open('http://localhost:8000/api/google_scholar/inteligencia%20artificial', '_blank');
  };

  const openOpenLibrary = () => {
    window.open('http://localhost:8000/api/open_library/programação', '_blank');
  };

  const openSemanticScholar = () => {
    window.open('http://localhost:8000/api/semantic_scholar/machine%20learning', '_blank');
  };

  const openWikipedia = () => {
    window.open('http://localhost:8000/api/wikipedia/unip', '_blank');
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1 className="app-title">UNIPENSE AI</h1>
        <p className="app-subtitle">Pesquisa Inteligente, Aprendizado Eficiente</p>
      </header>

      <main className="app-main">
        <div className="search-container">
          <form className="search-form">
            <input
              className="search-input"
              type="text"
              placeholder="Pesquise algo..."
            />
            <button className="search-button" type="submit">Pesquisar</button>
          </form>
        </div>

        {/* Botões de teste para os endpoints */}
        <div className="test-buttons-container">
          <button className="test-button" onClick={openGoogleScholar}>
            Testar Google Scholar
          </button>
          <button className="test-button" onClick={openOpenLibrary}>
            Testar Open Library
          </button>
          <button className="test-button" onClick={openSemanticScholar}>
            Testar Semantic Scholar
          </button>
          <button className="test-button" onClick={openWikipedia}>
            Testar Wikipedia
          </button>
        </div>
      </main>

      <footer className="app-footer">
        <p>&copy; 2025 UNIPENSE AI. Todos os direitos reservados.</p>
      </footer>
    </div>
  );
}

export default App;
