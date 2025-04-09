from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, "base.html")


def home(request, idx: int):

    ctx = {
        "valor": idx
    }

    return render(request, "home.html", ctx)