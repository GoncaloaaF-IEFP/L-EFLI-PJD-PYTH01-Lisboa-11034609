from modelos import *
from Pessoa import Pessoa

prof = Professor("nome prof", 21, "email p", "10793")
al = (Aluno("nome a", 15, "email a", "Py"))
p = Pessoa("nome p", 21, "mail p")


print(prof)

prof.envelhecer()
print(prof)

prof.envelhecer(anos=21)
print(prof)

prof.envelhecer(10)
print(prof)

print("----"*10)
print(al)

prof.envelhecer(10)
lst = [al, prof, p]

print("-----for-----"*10)
for i in lst:
    print(i.envelhecer())
print("-----for-----"*10)

print(isinstance(prof, Pessoa))
print(isinstance(prof, Professor))
print(isinstance(prof, Aluno))

prof2 = prof

print(prof2 is prof)