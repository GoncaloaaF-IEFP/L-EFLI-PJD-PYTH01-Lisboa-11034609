from fastapi import FastAPI
from typing import Optional

app = FastAPI()


"""
api para lidar com alunos e notas de alunos


get - 

lista Alunos
info Aluno com id x
    lista todas as notas de todos aluno
    lista todas as notas do aluno com id x
    lista todas as notas de todos aluno na UFCD com cod x
    lista todas as notas do aluno com id y na UFCD com cod x




/alunos -> devolve uma lista com todos os alunos
/alunos/{id} -> devolve um aluno
/alunos/notas -> devolve todas as notas de todos os alunos
/alunos/{id}/notas -> devolve todas as notaa de um aluno


/notas?id={id_nota}&aluno={id_aluno}&ufcd={id_ufcd}  -> devolve a 
                                                            nota com id id_nota, 
                                                            do aluno com id id_aluno,
                                                            da UFCD com id id_ufcd


/notas?id=&aluno={id_aluno}&ufcd={id_ufcd}  -> devolve a todas as notas
                                                            do aluno com id id_aluno,
                                                            da UFCD com id id_ufcd


/notas?id=&aluno={id_aluno}&ufcd=  -> devolve a todas as notas
                                                            do aluno com id id_aluno,


/notas?id=&aluno=&ufcd={id_ufcd}  -> devolve a todas as notas
                                                            da UFCD com id id_ufcd
                 
                                                                           
/notas?id={id_nota}&aluno=&ufcd=  -> devolve a nota com id id_nota

                                                         
/notas?id=&aluno=&ufcd=  ou /notas -> devolve todas as notas




post - 

Criar aluno

Criar nota de aluno

Criar notas em um aluno

Criar nota de alunos - permite adicionar um nota em mais de um aluno ao mesmo tempo, 
recebe 
    um arry "obj, json"  com o id do aluno e a nota, exp [{id: 1, nota: 10}, {id: 2, nota: 15}]


Criar notas em um alunos



"""


"""


/alunos/notas -> devolve todas as notas de todos os alunos
/alunos/{id}/notas -> devolve todas as notaa de um aluno
"""



"""
/alunos -> devolve uma lista com todos os alunos

"""
@app.get("/alunos")
async def alunos():
    return {"message": "Hello World"}



"""
/alunos/{id} -> devolve um aluno

"""
@app.get("/alunos/{id}")
async def aluno(id: int):
    return {"message": f"Hello {id}"}



"""
/alunos/{id}/notas -> devolve todas as notaa de um aluno

"""
@app.get("/alunos/{id}/notas")
async def aluno(id: int):
    return {"message": f"Hello {id}"}



"""
/alunos/notas -> devolve todas as notaa de todos os alunos

"""
@app.get("/alunos/notas")
async def aluno(id: int):
    return {"message": f"Hello {id}"}




"""

/notas?id={id_nota}&aluno={id_aluno}&ufcd={id_ufcd}  -> devolve a 
                                                            nota com id id_nota, 
                                                            do aluno com id id_aluno,
                                                            da UFCD com id id_ufcd


/notas?id=&aluno={id_aluno}&ufcd={id_ufcd}  -> devolve a todas as notas
                                                            do aluno com id id_aluno,
                                                            da UFCD com id id_ufcd


/notas?id=&aluno={id_aluno}&ufcd=  -> devolve a todas as notas
                                                            do aluno com id id_aluno,


/notas?id=&aluno=&ufcd={id_ufcd}  -> devolve a todas as notas
                                                            da UFCD com id id_ufcd
                 
                                                                           
/notas?id={id_nota}&aluno=&ufcd=  -> devolve a nota com id id_nota

                                                         
/notas?id=&aluno=&ufcd=  ou /notas -> devolve todas as notas
"""
@app.get("/notas")
async def get_nota(ufcd: Optional[int] = None, id: Optional[int] = None ,aluno: Optional[int]= None):
    return {"message": f"Hello {id}"}
