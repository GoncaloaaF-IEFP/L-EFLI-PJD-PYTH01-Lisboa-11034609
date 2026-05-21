from pydantic import BaseModel
from uuid import UUID, uuid4, uuid1


class Aluno(BaseModel):
    nome: str
    nome: str
    idade: int
    email: str