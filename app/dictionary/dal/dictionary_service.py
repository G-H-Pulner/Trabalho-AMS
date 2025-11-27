from app.dictionary.models.dictionary import Dictionary as DictionaryModel
from app.db.database import SessionLocal
from app.dictionary.schemas.dictionary import DictionaryCreate

def create_dictionary(dictionary: DictionaryCreate):
    db = SessionLocal()
    db_dictionary = DictionaryModel(**dictionary.model_dump())
    db.add(db_dictionary)
    db.commit()
    db.refresh(db_dictionary)
    db.close()
    return db_dictionary

def get_dictionary_by_id(dictionary_id: int):
    db = SessionLocal()
    dictionary = db.query(DictionaryModel).filter(DictionaryModel.id == dictionary_id).first()
    db.close()
    return dictionary

def get_dictionaries():
    db = SessionLocal()
    dictionaries = db.query(DictionaryModel).all()
    db.close()
    return dictionaries

def update_dictionary(dictionary_id: int, dictionary_data: DictionaryCreate):
    db = SessionLocal()
    db_dictionary = db.query(DictionaryModel).filter(DictionaryModel.id == dictionary_id).first()
    
    if db_dictionary:
        db_dictionary.assunto = dictionary_data.assunto
        db_dictionary.palavra = dictionary_data.palavra
        db_dictionary.acepcao = dictionary_data.acepcao
        db_dictionary.exemplo = dictionary_data.exemplo
        db_dictionary.classe_gramatical = dictionary_data.classe_gramatical
        db_dictionary.exemplo_libras = dictionary_data.exemplo_libras
        db_dictionary.origem = dictionary_data.origem
        
        db.commit()
        db.refresh(db_dictionary)
    
    db.close()
    return db_dictionary

def delete_dictionary(dictionary_id: int):
    db = SessionLocal()
    db_dictionary = db.query(DictionaryModel).filter(DictionaryModel.id == dictionary_id).first()
    
    if db_dictionary:
        db.delete(db_dictionary)
        db.commit()
    
    db.close()
    return db_dictionary