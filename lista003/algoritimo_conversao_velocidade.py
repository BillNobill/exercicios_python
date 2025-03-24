print("|-------------Conversão de Velocidade-------------|")
valorInserido = input("Insira um velocidade em km/h: ")

print("")

valorConvertido = round(float(valorInserido) / 3.6, 2)

print(f"O valor de {valorInserido} km/h em m/s é: {valorConvertido}")