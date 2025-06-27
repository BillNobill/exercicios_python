listaArrecadacao = [10, 20, 30, 40, 50]

def totalArrecadado(lista):
    total = 0
    
    for valor in lista:
        total += valor
    
    print("o total arrecadado foi: " + str(total))
    
totalArrecadado(listaArrecadacao)