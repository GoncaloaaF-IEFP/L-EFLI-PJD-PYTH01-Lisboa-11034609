"""

int - num inteiros
float - num decimal
str - string - texto
bool - booleano - True/False


"""
from erfa import atoiq

# cmt linha

"""
cmt multi linha
linha 2
linha 3

"""

# variaveis
idade = 38 # int
nome = "FeRnAnDo" # str
altura = 1.75  # float
aprvado = True # bool

# idade = "dez"

print(nome)

print("o " + nome.capitalize() + " tem " + str(idade) + " anos")

print("o", nome.capitalize(), "tem", idade, "anos")

print(f"o {nome.capitalize()} tem {idade} anos")
"""
#ler dados do teclado
nome2 = input("Digite seu nome: ")
print(f"Seja bem vindo {nome2.capitalize()}")
"""
#op

v1 = 10
v2 = 20

soma = v1 + v2
print(soma)

div = v1 / v2
print(div)


resto = v1 % v2
print(resto)


div1 = v1 // 3 # divisao inteira
print(div1)

div1 = v1 / 3 # divisao decimal
print(div1)

print(2 ** v1)


print("--txt--" * 5)

# print("--txt--" - "--") <- nao funciona

print("10" + "20")

# print("10" + 20)  <- nao funciona


# cast

idade = 10
idade_srt = str(idade)

nome = "10"
nome_int = int(nome)
print(nome_int)



# input 2

nome2 = input("Digite um num: ")
print(int(nome2))

nome2 = int(input("Digite um num: "))
#codigo.....
print(nome2)

