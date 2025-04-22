from django.contrib import admin
from .models import Aluno, Morada, UFCD, cartaoCidadao

# Register your models here.


admin.site.register(Aluno)
admin.site.register(Morada)
admin.site.register(UFCD)
admin.site.register(cartaoCidadao)