# listas (arrays)

arr = ["val1", "val2", "val3"]
print(arr[1])


arr.append('val4')
print(arr)

arr.insert(1, "val5")
print(arr)


print(arr.count("val4"))
arr.append('val4')
arr.append('val4')
arr.append('val4')

print(arr.count("val4"))

print("--- list size ---")
print(arr.__len__())
print(len(arr))


print("-----------------")
print(arr)
arr[1] = "Novo valor"
print(arr)
print("-----------------")

lista2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
arr.extend(lista2)
print(arr)
print(arr + lista2)

print("-----------------")

arr = ["val1", "val2", "val3", "val2"]

print(arr.index("val2")) # -> 1 ocur

#print(arr.index("val5"))

print("-----------------")

"""
cria
add
mostrar v1
esditar
remove 

"""

print("----- remover -----")
print(arr)


arr.remove("val2")
print(arr)

arr.remove("val2")
print(arr)

#arr.remove("val2")
# print(arr)


print("----- remover v2 -----")

arr = ["val0", "val1", "val2", "val3", "val4", "val5", "val6", "val7", "val8"]

print(arr)


arr.pop()

print(arr)

arr.pop(4)

print(arr)


print("----- list slice-----")

arr = ["val0", "val1", "val2", "val3", "val4", "val5", "val6", "val7", "val8"]

print(arr)

print(arr[:]) # lista toda

print(arr[0:4]) # val do 0 ao 3 -> arr[n:m] -> da pos n ate m-1


print(arr[4:7])

print(arr[::2]) # val da pos 0 ate a ultima de 2 em 2

print(arr[0:7:2])


print("----- get elm v2 -----")

print(arr[-1])

newArr = arr[::-1]
print(newArr)

print("-----------Copiar -----------")

arr = ["val1", "val2", "val3"]

novoArr2 = arr # duplciar a ref para a lisr

print(arr)
print(novoArr2)

novoArr2[0] = "Novo valor"

print(novoArr2)
print(arr)

print("---------")

arr = ["val1", "val2", "val3"]

novoArr2 = arr.copy() # duplciar a ref para a lisr


print(arr)
print(novoArr2)

novoArr2[0] = "Novo valor"

print(novoArr2)
print(arr)


print("---------")


def dupplicaElm(abc: list):
    abc[1] = "novo val func"


print(arr)
dupplicaElm(arr)
print(arr)


print("---- in -----")


print("val1" in arr) # verifica se o val esta na lista
print("Val1" in arr)


print("---- prec  lista  -----")


novaLista = []

for elm in arr:
    if elm.__len__() < 5:
        novaLista.append(elm.__len__())

print(novaLista)


print("------")

nomes = ["Carlos", "clara", "Cristina",
         "João", "Marcos", "Pedro", "Rui",
         "Ana", "Beatriz", "Sofia"]

nomes_c = []

for nome in nomes:
    if nome.capitalize().startswith("C"):
        nomes_c.append(nome)

print(nomes_c)


print("---- List comp -----")

nomes_cV2 = [nome for nome in nomes if nome.capitalize().startswith("C")]
print(nomes_cV2)

demo = ["Ola" for nome in nomes if nome.capitalize().startswith("C")]
print(demo)


myList = [1, "txt", True]
print(myList)


#tuplos
print("----- tuplos ----")
tp = ("val0", "val1", "val2", "val3")

print(tp)
print(tp[0])

for t in tp:
    print(t)

print(tp.__len__())
print(len(tp))

print("---- mudar valor -----")

## tp[0] = "Novo valor" <- nao funciona,  tuplo é estatico

aux = list(tp)
aux[0] = "Novo valor"
tp = tuple(aux)
print(tp)


print("----unpack tuplo ----")

(v1, v2, v3, v4) = tp


print(v1)
print(v2)
print(v3)
print(v4)

# Set
print("-----Set ----")

mySet = {"val0", "val1", "val2", "val3", "val4"} # nao tem ordem

print("val0" in mySet)

print("val0" not in mySet)

print("val10" not in mySet)

print("---------")


for elm in mySet:
    print(elm)



print("---------")

print(mySet.__len__())
mySet.add("val5")
print(mySet.__len__())
mySet.add("val5")
print(mySet.__len__())




print("----- set op -----")

mySet = {"val0", "val1", "val2", "val3", "val4"}
mySet2 = {"val3", "val4", "val5", "val6", "val7"}


print("mySet:", mySet)
print("mySet2:", mySet2)

print(mySet.union(mySet2))
mySet.update(mySet2)
print("mySet:", mySet)


mySet = {"val0", "val1", "val2", "val3", "val4"}
mySet2 = {"val3", "val4", "val5", "val6", "val7"}

inter = mySet.intersection(mySet2)
print("inter", inter)

dif1 = mySet.difference(mySet2)
print("dif1", dif1)

dif2 = mySet2.difference(mySet)
print("dif2", dif2)

dif_sym = mySet.symmetric_difference(mySet2)
print("dif_sym", dif_sym)



mySet.symmetric_difference_update(mySet2)
print("dif sym mySet: ", mySet)

# dict
print("---- dict -----")

myDict = {"key1": "Valor1",
          "key2": "Valor2",
          "key3": "Valor3"
          }

print("myDict: ", myDict)

print(myDict["key1"])

myDict["key4"] = "Valor4"

print("myDict: ", myDict)

# print(myDict["key5"]) <- key nao existe = Erro

print(myDict.get("key2"))
print(myDict.get("key5")) # <- key nao existe = None


myDict["key1"] = "Novo valor"

print("\n\n")
print("myDict: ", myDict)

print("print(myDict.popitem())")
print(myDict.popitem())

print("\n")
print("print(myDict.pop(\"Key1\"))")

print("myDict: ", myDict)
print(myDict.pop("key1"))

print("myDict: ", myDict)

print("---- loop dict -----")


for elm in myDict:
    print(elm)


print("-----")
for elm in myDict.keys():
    print(elm)


print("-----")
for elm in myDict.values():
    print(elm)

print("-----")
for elm in myDict.items():
    (key, val) = elm
    print(f"key: {key}, value: {val}")


print("-----")
print("keys: ", myDict.keys())
print("keys: ", myDict.values())
print("keys: ", myDict.items())





