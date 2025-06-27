lista = []

for i in range(10):
    lista.append(int(input("Digite um número: ")))
    
print("Os números em ordem crescente são:")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

lista = bubble_sort(lista)
print(lista)