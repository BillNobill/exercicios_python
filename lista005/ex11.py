nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
idades = [15, 30, 12, 28, 35]

print("Os maiores de idade são:")
for i in range(len(nomes)):
    if idades[i] >= 18:
        print(f"{nomes[i]} ({idades[i]} anos) - Maior de idade")
    elif idades[i] < 18:
        print(f"{nomes[i]} ({idades[i]} anos) - Menor de idade")