print("|-------------Verificação do IMC-------------|")
peso = input("Digite seu peso em KG: ")
altura = input("Digite sua altura em metros: ")

print("")

imc = float(peso) / (float(altura) ** 2)
imc = round(imc, 2)

if imc < 18.5:
    print(f"Seu imc é {imc} e você está abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print(f"Seu imc é {imc} e você está com o peso normal")
elif imc >= 25 and imc < 30:
    print(f"Seu imc é {imc} e você está com sobrepeso")
else:
    print(f"Seu imc é {imc} e você está com obesidade")


