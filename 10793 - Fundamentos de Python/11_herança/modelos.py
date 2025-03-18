from Pessoa import Pessoa


class Aluno(Pessoa):

    def __init__(self, nome, idade, email, turma):
        self.turma = turma
        super().__init__(nome, idade, email)

    def mudar_turma(self, nova_turma: str):
        self.turma = nova_turma


class Professor(Pessoa):
    def __init__(self, nome, idade,email, UFCD):
        self.UFCD = UFCD
        super().__init__(nome, idade, email)

    def mudar_UFCD(self, nova_UFCD: str):
        self.UFCD = nova_UFCD

    def __str__(self):
        msg = f"""------------
"nome placeholder"\n{self.idade}\n{self.email}\n{self.UFCD}
------------"""

        return msg