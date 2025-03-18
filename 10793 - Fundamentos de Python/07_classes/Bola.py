"""
 Crie uma classe que modele uma bola:
Classe Bola:            - Done
   - Atributos:
        cor             - Done
        circunferencia  - Done
        material        - Done
   - Métodos:
        troca_cor
        mostra_cor

"""

class Bola:
    def __init__(self, cor: str, circunferencia: float, material: str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor: str):
        self.cor = nova_cor

    def mostra_cor(self):
        return self.cor

    def msg_com_cor(self):
        return f"A cor da bola é {self.cor}"

    #def mostra_cor_v2(self):
    #    print(self.cor)
