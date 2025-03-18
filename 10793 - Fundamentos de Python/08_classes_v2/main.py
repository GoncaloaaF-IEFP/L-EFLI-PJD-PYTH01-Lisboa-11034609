from  morada import Morada

m1 = Morada("rua 1", "10A", "4f", "1100-412", "Lisboa")
m2 = Morada("rua 1", "10A", "4f", "1100-412", "Lisboa")



# print(m1)


s = str(m1)

print(s)
print(type(s))
print(type(m1))

print("-------"*3)
m3 = m1 # m3 e o mesmo que m1
print(m1)
print("----")
print(m3)
print("-------"*3)

m3.rua = "Rua 3"

print(m3)
print("----")
print(m1)


print("-----------"*3)

m1 = Morada("rua 1", "10A", "4f", "1100-412", "Lisboa")
m2 = Morada("rua 1", "10A", "4f", "1100-412", "Lisboa")

print(m1 == m1)
print(m1 == m2)
print(m1 == m3)
print(m3.rua)


print("-----------"*3)

m1 = Morada("rua 1", "10", "4d", "1100-412", "Lisboa")
m2 = Morada("rua 1", "10A", "412", "1100-412", "Lisboa")
m3 = Morada("rua 1", "112", "4f", "1100-412", "Lisboa")

print(m1 == m1)
print(m1 == m2)
print(m1 == m3)
