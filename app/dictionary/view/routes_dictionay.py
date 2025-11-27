from fastapi import APIRouter, HTTPException, status
from typing import List
from app.dictionary.schemas.dictionary import Dictionary, DictionaryCreate
from app.dictionary.dal.dictionary_service import (
    create_dictionary, 
    get_dictionary_by_id,
    get_dictionaries,
    update_dictionary,
    delete_dictionary
)

router = APIRouter(prefix="/dictionarys", tags=["dictionarys"])

# 1. CREATE
@router.post("/", response_model=Dictionary, status_code=status.HTTP_201_CREATED)
def create(dictionary: DictionaryCreate):
    return create_dictionary(dictionary)

# 2. READ ALL (Lista todos)
@router.get("/", response_model=List[Dictionary])
def read_all():
    return get_dictionaries()

# 3. READ ONE (Pega um pelo ID)
@router.get("/{dictionary_id}", response_model=Dictionary)
def read(dictionary_id: int):
    dictionary = get_dictionary_by_id(dictionary_id)
    if not dictionary:
        raise HTTPException(status_code=404, detail="Dictionary not found")
    return dictionary

# 4. UPDATE (Atualiza pelo ID)
@router.put("/{dictionary_id}", response_model=Dictionary)
def update(dictionary_id: int, dictionary_data: DictionaryCreate):
    updated_dictionary = update_dictionary(dictionary_id, dictionary_data)
    if not updated_dictionary:
        raise HTTPException(status_code=404, detail="Dictionary not found")
    return updated_dictionary

# 5. DELETE (Deleta pelo ID)
@router.delete("/{dictionary_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(dictionary_id: int):
    dictionary = get_dictionary_by_id(dictionary_id)
    if not dictionary:
        raise HTTPException(status_code=404, detail="Dictionary not found")
    
    delete_dictionary(dictionary_id)
    return None # Retorna vazio no 204