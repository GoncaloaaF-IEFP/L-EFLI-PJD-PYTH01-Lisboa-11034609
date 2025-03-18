from morada import Morada

m1 = Morada("rua 1", "10", "4d", "1100-412", "Lisboa", 10)
m2 = Morada("rua 1", "10A", "412", "1100-412", "Lisboa", 20)



print(m1 > m2)
print(m2 > m1)

print(m1 < m2)
print(m2 < m1)


print(m2 == m1)


print("------" * 5)

print(m1.__dict__)
"""

{
    'rua': 'rua 1', 
    'cp': '1100-412', 
    'porta': '10', 
    'apt': '4d', 
    'localidade': 'Lisboa', 
    'distancia': 10
}


"""