from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Dictionary(Base):
    __tablename__ = "dictionary"

    id = Column(Integer, primary_key=True, index=True)
    assunto = Column(String)
    palavra = Column(String)
    acepcao = Column(String)
    exemplo = Column(String)
    classe_gramatical = Column(String)
    exemplo_libras = Column(String)
    origem = Column(String)
    mao = Column(String)
    imagem = Column(String)
    video = Column(String)