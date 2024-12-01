from pydantic import BaseModel
from typing import List

class PostoVacinacao(BaseModel):
    id: int = 0
    cidade: str
    nome: str
    endereco: str
    horario: str
    vacinas: List[str] = []