import sqlite3
import sys

bd = sqlite3.connect('demo.db') # abre a ligação
bd.row_factory = sqlite3.Row
curr = bd.cursor()



curr.execute("""Create Table if not exists Alunos2(
        id integer primary key autoincrement ,
        nome varchar(50),
        turma varchar(50),
        email varchar(80)
        )
""")





"""
print(f"data size: {sys.getsizeof(data)}")
res = data.fetchone()
print(res)
print(f"data.fetchone() size: {sys.getsizeof(res)}")
print(f"data size: {sys.getsizeof(data)}")
print(data.fetchone())
print(f"data size: {sys.getsizeof(data)}")
"""

pre_prep_SQL ="insert into Alunos values (?, ?, ?, ?);"

curr.execute(pre_prep_SQL, (25, 'nome 20', 'turma 20' , 'email15@mail.com'))

bd.commit()


curr.executemany(pre_prep_SQL, [
(21, 'nome 21', 'turma 20' , 'email21@mail.com'),
(22, 'nome 22', 'turma 20' , 'email22@mail.com'),
(23, 'nome 23', 'turma 20' , 'email23@mail.com')

])

bd.commit()


data = curr.execute("""Select * from Alunos""")

# res = data.fetchmany(3)

# print(dict(res[0]))

res = data.fetchall()

for i in res:
    print(dict(i))






bd.close() # fecha a ligação
