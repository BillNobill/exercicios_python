valores = [50, 30, 70, 90]

def comissao(valores):
    soma = 0
    for valor in valores:
        soma += valor * 0.1
    return soma

print("A comissão do vendedor é: " + str(comissao(valores)))