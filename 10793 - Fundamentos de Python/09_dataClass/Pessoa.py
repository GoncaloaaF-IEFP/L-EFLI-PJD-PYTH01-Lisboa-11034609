from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int

    def func(self):
        pass

class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade