nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

print("Os nomes com mais de 5 letras são")

for i in range(len(nomes)):
    if len(nomes[i]) > 5:
        print(nomes[i])