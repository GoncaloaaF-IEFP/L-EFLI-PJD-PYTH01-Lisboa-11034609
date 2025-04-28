from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Aluno


# Create your views here.

def index(request):

    ctx = {
        "nome": "Gonçalo",
        "email": "goncalo@mail.pt",
    }

    return render(request, 'main/index.html', ctx)


def lista_alunos(request):
    al = Aluno.objects.all()

    ctx = {
        "lista_alunos": al,
    }

    return render(request, "main/lista.html", ctx)



def get_aluno(request, id:int):
    #al = Aluno.objects.get(id=id)
    al =  get_object_or_404(Aluno, id=id)
    ctx = {
        "aluno": al,
    }

    return render(request, "main/aluno.html", ctx)




def add_aluno(request):
    aluno = Aluno()
    aluno.nome = "Nome_1"
    aluno.email = "email_1@foo.pt"
    aluno.idade = 10

    aluno.save()

    return redirect("/")