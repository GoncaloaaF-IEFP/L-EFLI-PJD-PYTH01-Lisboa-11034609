from Livro import Livro
from Carro import Carro
import Bola as b

l1 = Livro("Python Rocks!", "Geek University", 2019)


print(l1.titulo)
print(l1.autor)
print(l1.ano)


c = Carro("Ford", "Fiesta", 2019)
c.andar()
c.travar()
print(c.get_estado())


c2 = Carro("Ford", "Mustang", 2019)
c2.andar()
c2.travar()

print(c2.get_estado())
c2.ligar()
print(c2.get_estado())

print("--" * 10)

bola1 = b.Bola("Azul", 10, "Plástico")
print(bola1.mostra_cor())
bola1.troca_cor("Vermelho")
print(bola1.msg_com_cor())