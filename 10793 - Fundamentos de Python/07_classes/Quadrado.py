"""

Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos:
        Tamanho do lado - ok
    Métodos:
    Mudar valor do Lado - ok
    Retornar valor do Lado  - ok
    calcular Área;
"""

class Quadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def troca_lado(self, novo_lado: float):
       self.novo_lado = novo_lado

    def mostra_cor(self):
        return self.novo_lado

    def caclula_area(self):
        return pow(self.lado, 2)
        #return self.novo_lado ** 2
        #return self.novo_lado * self.novo_lado