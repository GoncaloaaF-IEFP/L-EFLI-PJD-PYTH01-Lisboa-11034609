"""

var
tipos de dados
cond
    if
    match-case
range
loops
    for
    while


"""


# void olaMundo(){}

def olaMundo():
    print("Ola Mundo")

olaMundo()


def ola_mundo2(nome):
    print(f"Ola Mundo, {nome}")


ola_mundo2("Gonçalo")
ola_mundo2(2025)


def ola_mundo3(nome, ano):
    print(f"Ola Mundo, {nome} em {ano}")

ola_mundo3("Gonçalo", 2025)
ola_mundo3(2025, True)


def ola_mundo4(nome: str, ano: int):
    print(f"Ola Mundo, {nome.capitalize()} em {ano}")


ola_mundo4("joão", 2025)

# ola_mundo4(2025, "Joao")

"""

em C qual o tipo de param?

tipoDados -char : 
    s - "string"
    i - int
    f - float


func nome(param, char tipoDados){
    se param Int
        ......
        return 
    se param str
        ......
        return

}



"""


def ola_mundo5(nome, ano):
    return f"Ola Mundo, {nome} em {ano}"


ola_mundo5("Gonçalo", 2001)

msg = ola_mundo5("Gonçalo", 2001)

print(msg)

print(ola_mundo5("Gonçalo 2", 2001))

"""
tem de utilizar funções:

1 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
2 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês.
3 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).

"""

print("--" * 10)


def ola_mundo6(nome: str, ano: int):
     print(f"Ola Mundo, {nome} em {ano}")


ola_mundo6(nome="Gonçalo", ano=2025)

ola_mundo6(ano=2025, nome="Gonçalo")

ola_mundo6("Gonçalo", ano=2025)


def ola_mundo7(nome: str, ano: int, ano2: int):
    print(f"Ola Mundo, {nome} em {ano} e {ano2}")


ola_mundo7("Jose", ano=2025, ano2=2001)

ola_mundo7("Jose", ano2=2025, ano=2001)


ola_mundo7("Jose", 2001,ano2=2025)

print("--" * 10)

def ola_mundo8(nome: str, ano: int = 2025, ano2: int = 2001):
    print(f"Ola Mundo, {nome} em {ano} e {ano2}")

ola_mundo8("Jose", ano=1990, ano2=2022)
ola_mundo8("Rui")

ola_mundo8("Rui", 2131)



def soma(num1: int, num2: int) -> int:
    #validar se o input e int
    return num1 + num2


def soma_v2(num1, num2):
    return num1 + num2


print(soma(12,12))
print(soma_v2(12,12))


print(soma(12.5,12.5))
print(soma_v2(12.5,12.5))


print(soma("abc","cba"))
print(soma_v2("abc","cba"))