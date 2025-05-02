from pydantic import BaseModel

class UFCD(BaseModel): # -> 38bytes
    nome: str # Programação avançada com Python
    id: int   # 10794

class Nota(BaseModel):
    nota1: float
    ufcd: UFCD
    id_aluno: int


class Aluno(BaseModel):
    nome: str
    idade: int
    notas: list[Notas]
