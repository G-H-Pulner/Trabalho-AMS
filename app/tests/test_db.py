from app.db.database import engine, Base
from app.dictionary.models.dictionary import Dictionary

Base.metadata.create_all(bind=engine)
print("Banco criado com sucesso!")