from pydantic import BaseModel

class DictionaryBase(BaseModel):
    assunto: str | None = None
    palavra: str
    acepcao: str | None = None
    exemplo: str | None = None
    classe_gramatical: str | None = None
    exemplo_libras: str | None = None
    origem: str | None = None
    mao: str
    imagem: str | None = None
    video: str | None = None

class DictionaryCreate(DictionaryBase):
    pass

class Dictionary(DictionaryBase):
    id: int

    class Config:
        from_attributes = True