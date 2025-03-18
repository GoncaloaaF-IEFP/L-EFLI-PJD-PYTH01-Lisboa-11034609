class Carro:
    def __init__(self, marca:str, ano:int):
        self.__marca = marca
        self.__ano = ano
        self.__modelo = "modelo"

    @property
    def modelo(self):
        return self.__modelo.upper()

    @property
    def marca(self):
        return self.__marca

    def setMarca(self, marca: str):
        self.__marca = marca

    def calc_idade(self) -> int:
        return 2025 - self.__ano

    @property
    def idade(self):
        return 2025 - self.__ano

    @property #usar o output de uma func como se fosse um var. deve ser usado para ler uma var de forma mais segura
    def ano(self):
        return self.__ano

    @ano.setter #usar o usar uma func com um param como se fosse uma var, deve ser usado para escrever num var de forma mais segura
    def ano(self, ano: int):
        self.__ano = ano
