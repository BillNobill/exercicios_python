vetor = [12, 24, 31, 48, 59]

def buscarVetor(vetor):
    for valor in vetor:
        if valor == 31:
            return print("Valor encontrado!")
    else:
        return print("Valor não encontrado!")
    
buscarVetor(vetor)