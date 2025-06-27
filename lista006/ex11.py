lista = [10, 20, 30, 40, 50]

def busca_sequencial(lista, valor):
    quantidadeBuscas = 0
    for i in lista:
        quantidadeBuscas += 1
        print(f"Buscando {i} na lista... (busca número {quantidadeBuscas})")
        if i == valor:
            return True
    return False

print(busca_sequencial(lista, 30))