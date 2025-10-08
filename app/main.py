from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os
import psycopg2

app = FastAPI()

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_connection():
    required_vars = ["DB_NAME", "DB_USER", "DB_PASS", "DB_HOST", "DB_PORT"]
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Variável de ambiente ausente: {var}")

    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/", response_class=HTMLResponse)
def read_root():
    return FileResponse("static/index.html")

@app.get("/db-check")
def check_db_connection():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT version();")
                version = cur.fetchone()
        return {"status": "Conectado ao banco!", "versao": version}
    except Exception as e:
        return {"status": "Erro de conexão", "detalhes": str(e)}
