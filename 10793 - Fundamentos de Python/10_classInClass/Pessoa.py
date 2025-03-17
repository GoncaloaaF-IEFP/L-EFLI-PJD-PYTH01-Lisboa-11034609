from dataclasses import dataclass

"""
telefone
emial

"""
@dataclass
class Contacto:
    telefone: str
    emial: str
    def __init__(self, telefone, emial):
        self.telefone = telefone
        self.emial = emial


"""
nome
contato

"""
@dataclass
class Pessoa:

    def __init__(self, nome, telefone, emial):
        self.nome = nome
        self.listaCts = []
        contato = Contacto(telefone, emial)
        self.listaCts.append(contato)

    def add_contato(self, i):
        self.listaCts.append(Contacto(f"telefone {i}", f"email {i}"))


