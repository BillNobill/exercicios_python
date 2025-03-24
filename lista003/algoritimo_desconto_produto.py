print("|-------------Desconto em Produto-------------|")
valorPorduto = input("Insira o valor do produto para a aplicação de 10% de desconto: ")

print("")

valorComDesconto = round(float(valorPorduto) - float(valorPorduto) * 0.10, 2)

print(f"O valor com desconto é {valorComDesconto} reais.")