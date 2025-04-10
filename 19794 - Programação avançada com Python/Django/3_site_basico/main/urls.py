from django.urls import path
from . import views


app_name = "main"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_aluno, name="add" ),

    path("als/", views.lista_alunos, name="alunos"),

    path("aluno/<int:id>/", views.get_aluno, name="aluno"),

]