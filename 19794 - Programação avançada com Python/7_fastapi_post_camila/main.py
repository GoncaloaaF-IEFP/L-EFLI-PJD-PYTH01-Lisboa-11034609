from fastapi import FastAPI
from modelo import *
app = FastAPI()

lista_alunos = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/alunos")
async def get_alunos():
    return lista_alunos


@app.post("/alunos")
async def add_aluno(aluno: Aluno):
    #ver se já existe

    lista_alunos.append(aluno)
    return {"httpCode": 200, "message": "Ok" }



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
