for i in range(100):
    if i % 5 == 0:
        print(i)
        print("\tMultiplo de 5 -> go to next")

        continue

    if i % 2 == 0:
        print(i)
        print("\tpar")

    if i == 50:
        print("\tChegou a 50")
        break