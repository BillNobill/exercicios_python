print("|-------------Conversão de Moedas-------------|")
valorInserido = input("Insira um valor em reais (R$): ")
taxaCambio = 5.30

print("")

valorConvertido = round(float(valorInserido) / taxaCambio, 2)

print(f"O valor de {valorInserido} reais em doláres é: {valorConvertido}")