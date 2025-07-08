
from pydantic import BaseModel
from typing import List

class MatrizConhecimento(BaseModel):
    topicos: List[str]

class NotasAluno(BaseModel):
    nome: str
    notas: List[float]
