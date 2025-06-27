lista = []

for i in range(5):
    lista.append(int(input("Digite um número: ")))
    
print("O maior número da lista é" + str(max(lista)))
print("O menor número da lista é" + str(min(lista)))
print("A média dos valores é " + str(sum(lista) / len(lista)))