print("----Condições----")


# if ?

idade = 10

"""
if(idade > 18){ 
    printf("Maior de idade")
    printf("Maior de idade")
    printf("Maior de idade")
}

"""
idade = 20

if idade > 18:
    print("Adulto")
elif idade > 12:
    print("Adolescente")
else:
    print("Criança")


print("depoois do if")




"""
&& -> and
|| -> or
! -> not

"""

faltas = 0.1
nota = 18

if  not (nota >= 10 and faltas <= 0.1):
    print("Aprovado")
else:
    print("Reprovado")