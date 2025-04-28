from django.db import models

"""
 1 - 1 <-> one - one   <->  1:1
 1 - n <-> one - many  <-> 1:n
 n - m <-> many - many <-> m:n
"""


class cartaoCidadao(models.Model):
    numero = models.IntegerField(unique=True)


class Morada(models.Model):
     rua = models.CharField(max_length=120)
     cp = models.CharField(max_length=120) # 1234-341
     porta = models.CharField(max_length=120)
     apt = models.CharField(max_length=120)


class UFCD(models.Model):
    name = models.CharField(max_length=100)
    codifo = models.IntegerField()

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    cc = models.OneToOneField(cartaoCidadao, on_delete=models.CASCADE) # 1:1
    morada = models.ForeignKey(Morada, on_delete=models.CASCADE) #
    ufcd = models.ManyToManyField(UFCD)



