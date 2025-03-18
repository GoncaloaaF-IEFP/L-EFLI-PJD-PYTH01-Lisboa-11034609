
class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def envelhecer(self, anos:int = 1):
        self.idade += anos

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'