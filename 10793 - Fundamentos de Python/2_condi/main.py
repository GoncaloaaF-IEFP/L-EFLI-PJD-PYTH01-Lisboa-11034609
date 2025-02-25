'''

condições:
    if
    elif
    else

    and -> &&
    or -> ||
    not -> !

    == -> igual
    != -> diferente
    > -> maior
    < -> menor
    >= -> maior ou igual
    <= -> menor ou igual

    match -> switch case

'''

altura_Minima = 1.8
idade_Minima = 18

idade = 19
altura = 1.7


if idade >= idade_Minima and altura >= altura_Minima:
    print("Apto")
elif idade >= idade_Minima or altura >= altura_Minima:
    print("apenas um dos param é valido")
else:
    print("não Apto")




print(" 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante. \n")

"""
Faça um Programa que verifique se uma letra digitada é vogal ou nao vogal (consoante).



Vogais - aeiou
consoantes - resto

"""


letra = input("digite uma letra: ")
letra = letra.lower()


if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Vogal")
else:
    print("Consoante")



match letra:
    case "a":
        print("Vogal")
    case "e":
        print("Vogal")
    case "i":
        print("Vogal")
    case "o":
        print("Vogal")
    case "u":
        print("Vogal")
    case _:
        print("Consoante")


match letra:
    case "a" | "e" | "i" | "o" | "u":
        print("Vogal")
    case _:
        print("Consoante")




