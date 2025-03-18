txt = "Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"

for letra in txt:
    print(letra) # -> f"{letra}\n"

for letra in txt:
    print(letra, end= " - ") # -> f"{letra} - "