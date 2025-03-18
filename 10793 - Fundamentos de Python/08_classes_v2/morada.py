
class Morada:
    def __init__(self, rua:str, porta:str, apt:str, cp:str, localidade:str, distancia:float = 0):
        self.rua = rua
        self.cp = cp
        self.porta = porta
        self.apt = apt
        self.localidade = localidade
        self.distancia = distancia


    def __str__(self):
        return f"{self.rua}\n{self.porta} {self.apt}\n{self.cp}, {self.localidade}"


    def __eq__(self, other):
        if (    self.rua == other.rua and
                self.cp == other.cp and
                self.localidade == other.localidade):
            return True
        else:
            return False

    def __gt__(self, other): # maior que
        return self.distancia > other.distancia






