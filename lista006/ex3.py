listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mediaNumeros(lista):
    media = sum(lista) / len(lista) 
    print("A média dos números é: " + str(media))
    
mediaNumeros(listaNumeros)