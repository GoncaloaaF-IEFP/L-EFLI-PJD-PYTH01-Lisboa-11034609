from fastapi import FastAPI
from Aluno import Aluno

app = FastAPI()

"""
get - read
post - create


put - update
delete - delete


"""

@app.get("/") # /
async def root():
    return {"message": "Hello World"}



@app.get("/alunos") # /alunos
async def alunos():
    return {"ListaAlunos": [
            "Aluno1",
            "Aluno2",
            "Aluno3",
            "Aluno4",
        ]
        }

@app.get("/aluno/{id}") # /alunos/1 <- qd o id for obrigatorio
async def aluno(id: int):
    return {"detalhe":f"Aluno {id}" }


@app.get("/aluno/{id}/info") # /alunos/1 <- qd o id for obrigatorio
async def aluno(id: int):
    return {"infos":f"Aluno {id}" }


@app.get("/aluno/{id}/notas") # aluno/12/notas?ufcd=10794
                              # aluno/12/notas
async def aluno(id: int, ufcd: str = None):
    if ufcd:
        return {"notas":f"Notas do Aluno {id} na {ufcd}" }

    return {"notas":f"Todas as notas do Aluno {id}" }

@app.get("/hello") # /hello?name=ola <- qd o name nao for obrigatorio
async def say_hello(name: str):
    return {"message": f"Hello {name}"}




@app.post("/aluno")
async def add_alunos(aluno: Aluno):
    return {"aluno": aluno}


@app.post("/alunos/{id}/nota")
async def add_alunos(id:int, nota: float):
    return {"message": f"add nota {nota} ao aluno {id}"}



"""


{} <- obj
[] <- array
"nome" = "valor" <- key value   

"alunos": [
    {
        "nome": "Aluno1",
        "idade": 18,
        "endereco": "rua x"
        "inscrito": false
    }
]



alunos = list[Aluno]

class Aluno:
    nome: str
    idade: int
    endereco: str
    inscrito: bool







{
  "nome": "string",
  "email": "string",
  "notas": [
    {
      "nota": 0,
      "ufcd": {
        "nome": "string",
        "cod": 0
      }
    },
    {
      "nota": 0,
      "ufcd": {
        "nome": "string",
        "cod": 0
      }
    },
    {
      "nota": 0,
      "ufcd": {
        "nome": "string",
        "cod": 0
      }
    }
  ]
}



"""