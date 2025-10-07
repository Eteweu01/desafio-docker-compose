
# 🐳 Desafio Docker Compose - FastAPI + PostgreSQL

Este projeto faz parte do desafio de **Dockerfile, Docker Compose, redes e volumes**, configurando um ambiente multi-container funcional e seguro.

## 🚀 Estrutura do Projeto
```
├── Dockerfile
├── docker-compose.yml
├── .env
├── app/
│   ├── main.py
│   └── requirements.txt
```

## 🧩 Serviços
- **app**: API FastAPI rodando na porta `8000`
- **db**: Banco de dados PostgreSQL persistente

## ⚙️ Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/desafio-docker-compose.git
   cd desafio-docker-compose
   ```

2. Construa e inicie os containers:
   ```bash
   docker compose up -d --build
   ```

3. Acesse a aplicação:
   - API: [http://localhost:8000](http://localhost:8000)
   - Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

4. Teste a conexão com o banco:
   ```bash
   curl http://localhost:8000/db-check
   ```

## 🛠️ Configurações de Ambiente
Variáveis definidas no arquivo `.env`:
```
DB_USER=app_user
DB_PASS=app_password
DB_NAME=app_db
DB_HOST=db
DB_PORT=5432
```

## 💾 Persistência
Os dados do banco são mantidos mesmo após reiniciar os containers, graças ao volume configurado:
```yaml
volumes:
  db_data:
```

## 🔒 Segurança
- Usuário do banco **não é root**
- Variáveis sensíveis em `.env`
- Rede customizada isolando os containers

---
**Pronto!** Este projeto cumpre todos os 10 itens do checklist proposto.
