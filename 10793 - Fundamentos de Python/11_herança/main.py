from modelos import *

prof = Professor("nome p", 21, "email p", "10793")
al = (Aluno("nome a", 15, "email a", "Py"))


print(prof)

prof.envelhecer()
print(prof)

prof.envelhecer(anos=21)
print(prof)

prof.envelhecer(10)
print(prof)

print("----"*10)
print(al)