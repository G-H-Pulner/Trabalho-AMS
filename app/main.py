from fastapi import FastAPI
from app.db.database import engine, Base
from app.dictionary.models.dictionary import Dictionary 
from app.dictionary.view import routes_dictionay

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Dicionário")

app.include_router(routes_dictionay.router)

@app.get("/")
def read_root():
    return {"message": "Olá usuário"}