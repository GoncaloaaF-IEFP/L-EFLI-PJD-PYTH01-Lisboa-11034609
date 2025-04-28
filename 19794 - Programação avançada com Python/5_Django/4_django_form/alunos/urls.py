from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("config/", views.config),

    path("add/", views.add_aluno, name="add_aluno"),

]