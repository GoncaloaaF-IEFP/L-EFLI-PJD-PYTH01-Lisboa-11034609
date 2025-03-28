import faker
import sqlite3

faker = faker.Faker('pt_PT')

bd = sqlite3.connect('demo.db') # abre a ligação
bd.row_factory = sqlite3.Row
curr = bd.cursor()





pre_prep_SQL ="insert into Alunos2 (nome, turma, email) values (?, ?, ?);"

for i in range(0, 800000):
    curr.execute(pre_prep_SQL, (faker.name(), faker.distrito(), f"{faker.email()} {i}"))


bd.commit()