# while


i = 0
while i < 100:
    print(f"Hello, world! {i}")

    if i % 5 == 0:
        i += 4
        continue  # termina a iteração atual e vai para a próxima

    i += 1

    if i == 50:
        break
