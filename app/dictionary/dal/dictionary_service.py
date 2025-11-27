from app.dictionary.models.dictionary import Dictionary as DictionaryModel
from app.db.database import SessionLocal
from app.dictionary.schemas.dictionary import DictionaryCreate

def create_dictionary(dictionary: DictionaryCreate):
    db = SessionLocal()
    db_dictionary = DictionaryModel(
        assunto=dictionary.assunto, 
        palavra=dictionary.palavra, 
        acepcao=dictionary.acepcao,
        exemplo=dictionary.exemplo,
        classe_gramatical=dictionary.classe_gramatical,
        exemplo_libras=dictionary.exemplo_libras,
        origem=dictionary.origem
    )
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