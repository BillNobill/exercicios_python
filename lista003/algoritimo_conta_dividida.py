print("|-------------Valor por Pessoa de uma Conta Dividída-------------|")
valorTotal = float(input("Digite o valor total da conta em reais: "))
numPessoas = int(input("Digite o número de pessoas: "))

print("")

valorPorPessoa = valorTotal / numPessoas

print(f"O valor a pagar por pessoa é {valorPorPessoa} reais.")
