
class Pessoa:
    def __init__(self, nome, idade, email):
        self._nome = nome
        self.idade = idade
        self.email = email

    def envelhecer(self, anos:int = 1):
        self.idade += anos
        return f"{self._nome} envelheceu"

    def __str__(self):
        return f'Nome: {self._nome}, Idade: {self.idade}'