from fastapi import APIRouter, HTTPException, status
from app.dictionary.schemas.dictionary import Dictionary, DictionaryCreate
from app.dictionary.dal.dictionary_service import create_dictionary, get_dictionary_by_id

router = APIRouter(prefix="/dictionarys", tags=["dictionarys"])

@router.post("/", response_model=Dictionary, status_code=status.HTTP_201_CREATED)
def create(dictionary: DictionaryCreate):
    """
    Cria uma nova entrada no dicionário.
    """
    return create_dictionary(dictionary)

@router.get("/{dictionary_id}", response_model=Dictionary)
def read(dictionary_id: int):
    """
    Busca uma entrada pelo ID.
    """
    dictionary = get_dictionary_by_id(dictionary_id)
    if not dictionary:
        raise HTTPException(status_code=404, detail="Dictionary not found")
    return dictionary