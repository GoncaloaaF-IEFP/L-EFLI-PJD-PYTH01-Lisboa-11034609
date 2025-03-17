from Pessoa import Pessoa, Pessoa2

p = Pessoa("Gonçalo", 19)
p2 = Pessoa2("Gonçalo", 19)


print(p.nome)
print(p.idade)

print(p)

print(p.__dir__())
print(p2.__dir__())
