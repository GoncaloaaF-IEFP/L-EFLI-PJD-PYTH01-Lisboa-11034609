def msgDemo(func):

    def wrapper(*args, **kwargs):
        print("Inicio da Func")
        func(*args, **kwargs)
        print("Fim da Func")

    return wrapper



@msgDemo
def ola_Mundo(nome):
    print(f"Ola Mundo, {nome}")


@msgDemo
def ola_py():
    print("Ola Python")






ola_Mundo("Gonçalo")
print("-------")
ola_py()
