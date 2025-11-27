from pydantic import BaseModel

# Classe Base com os dados comuns
class DictionaryBase(BaseModel):
    assunto: str
    palavra: str
    acepcao: str
    exemplo: str
    classe_gramatical: str
    exemplo_libras: str
    origem: str

# Schema para validação na CRIAÇÃO (POST)
class DictionaryCreate(DictionaryBase):
    pass

# Schema para RETORNO dos dados (GET)
class Dictionary(DictionaryBase):
    id: int

    class Config:
        # Permite que o Pydantic leia dados direto do objeto do banco (SQLAlchemy)
        from_attributes = True