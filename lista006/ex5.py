listaNotas = [50, 70, 90]

def mediaNotas(lista):
    media = sum(lista) / len(lista)
    
    if (media < 70):
        print("Estude mais!")
    else:
        print("Aprovado com louvor!")
        
mediaNotas(listaNotas)