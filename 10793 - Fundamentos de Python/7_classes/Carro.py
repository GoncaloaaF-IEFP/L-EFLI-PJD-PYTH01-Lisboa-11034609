

class Carro:

    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.isLigado = False

    def ligar(self):
        print(f"{self.modelo} está a ligar...")
        self.isLigado = True

    def desligar(self):
        print(f"{self.modelo} está a desligar...")
        self.isLigado = False

    def andar(self):
        print(f"{self.modelo} está a andar...")

    def travar(self):
        print(f"{self.modelo} está a travar...")

    def get_estado(self):
        estado = ""

        if self.isLigado:
            estado = "ligado"
        else:
            estado = "desligado"

        return f"o {self.marca} {self.modelo} esta {estado}"
