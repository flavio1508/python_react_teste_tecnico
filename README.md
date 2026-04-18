# 📄 PDF Upload & Streaming App (Python + React)

Aplicação fullstack para upload, armazenamento e visualização de arquivos PDF.  
A solução foi desenvolvida com foco em simplicidade e funcionalidade, incluindo suporte a **streaming parcial (HTTP Range Requests)**.

---

## 🚀 Tecnologias utilizadas

### Backend
- Python
- Flask
- Flask-CORS

### Frontend
- React

### Comunicação
- HTTP / REST
- multipart/form-data (upload de arquivos)

---

## 📁 Estrutura do Projeto
/backend → API Flask (upload + streaming de PDF)
/frontend → Aplicação React (upload + visualização)

## ⚙️ Como executar o projeto

### 🔧 Backend e Frontend
cd backend
pip install flask flask-cors
python app.py

cd pdf-app
npm install
npm start

📌 Funcionalidades
Upload de arquivos PDF
Armazenamento local no servidor
Endpoint para visualização
Streaming parcial de arquivos (Range Requests)
Visualização direta no navegador
🧠 Explicação técnica (Streaming)

O backend implementa suporte ao header HTTP:

Range: bytes=start-end
🔄 Comportamento do servidor:

Quando o header Range está presente:

Interpreta o intervalo de bytes solicitado
Lê apenas o trecho necessário do arquivo

Retorna:

206 Partial Content
Define os headers:
Content-Range
Accept-Ranges
Content-Length

Quando o header Range não está presente:

O arquivo é retornado integralmente (download completo)
🖥️ Frontend

A visualização do PDF é feita utilizando:

<iframe>

O navegador:

Usa o visualizador nativo de PDF
Realiza requisições parciais automaticamente
Aproveita o streaming implementado no backend
⚡ Benefícios do Streaming
Carregamento progressivo do PDF
Melhor experiência do usuário
Ideal para arquivos grandes
Redução de consumo de banda
🔮 Possíveis melhorias para produção
Armazenamento em nuvem (ex: AWS S3)
URLs assinadas (signed URLs)
Autenticação e controle de acesso
Upload em partes (chunked upload)
Uso de CDN para distribuição
Validação mais robusta de arquivos (MIME real)
Logs e monitoramento
Visualizador avançado (ex: PDF.js)
✅ Considerações finais

A aplicação foi pensada para ser simples e funcional no contexto do teste, mas com uma base sólida para evolução.

O principal diferencial está na implementação de streaming parcial no backend, permitindo a visualização eficiente de arquivos PDF grandes sem necessidade de download completo.

<img width="783" height="373" alt="image" src="https://github.com/user-attachments/assets/be9a45f9-f620-4b67-87b9-dc46b0db05ad" />
