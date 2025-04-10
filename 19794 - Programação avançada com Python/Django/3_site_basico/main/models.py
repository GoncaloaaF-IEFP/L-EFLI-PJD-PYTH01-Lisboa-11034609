from django.db import models

# Create your models here.


class Aluno(models.Model):

    nome = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome