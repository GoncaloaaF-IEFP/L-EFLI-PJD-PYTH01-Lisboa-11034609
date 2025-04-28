from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Aluno
import faker

# Create your views here.


def config(request):
    f = faker.Faker('pt-PT')

    for _ in range(10):
        al = Aluno()
        al.nome = f.name()
        al.email = f.email()
        al.save()


    return redirect("/")



def index(request):
    alunos = Aluno.objects.all()


    ctx = {
        "alunos": alunos,
    }


    return render(request, "lista.html", ctx)



def add_aluno(request):

    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]

        al = Aluno()
        al.nome = nome
        al.email = email
        al.save()

        return redirect("/")


    return render(request, "form.html")