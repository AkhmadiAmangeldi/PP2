list = ["slad", "sdfa", "iafnh"]

with open('filefor5.txt', 'w') as file:
    for x in list:
        file.write(f"{x}\n")