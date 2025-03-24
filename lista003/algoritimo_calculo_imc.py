print("|-------------Verificação do IMC-------------|")
peso = input("Digite seu peso em KG: ")
altura = input("Digite sua altura em metros: ")

print("")

imc = float(peso) / (float(altura) ** 2)
imc = round(imc, 2)

print(f"Seu imc é {imc}!")