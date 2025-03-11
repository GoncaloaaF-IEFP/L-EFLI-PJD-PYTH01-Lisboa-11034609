"""

for


while


"""

# for(int i = 0; i> 10; i++){} <- c

# for each


"""
range(lb, up, s) -> lb até ao up-1, com um step de s
"""

range(10) # <-> range(0, 10) 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

range(5,10) # 5, 6, 7, 8, 9
range(5,10, 2) # 5, 7, 9



for idx, valor in enumerate(range(5, 100, 2)):
    print(f"{idx} - {valor}")

