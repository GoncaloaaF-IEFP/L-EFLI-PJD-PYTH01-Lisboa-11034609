
class Turma:
    def __init__(self):
        self.turmas = []

    def __add__(self, turma):
        self.turmas.append(turma)