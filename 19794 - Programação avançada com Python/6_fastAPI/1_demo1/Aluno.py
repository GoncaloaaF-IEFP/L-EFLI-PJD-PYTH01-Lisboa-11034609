from pydantic import BaseModel

class UFCD(BaseModel):
    nome: str
    cod: int


class Nota(BaseModel):
    nota: float
    ufcd: UFCD


class Aluno(BaseModel):
    nome: str
    email: str
    notas: list[Nota]