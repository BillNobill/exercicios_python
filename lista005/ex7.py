lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))
    
print("Os números que são maiores que 10 são:")
i = 1
for numero in lista:
    if numero > 10:
        print(str(f"{i}° {numero}"))
        i = i + 1
    
    

