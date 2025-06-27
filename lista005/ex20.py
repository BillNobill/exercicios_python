from random import shuffle

numeros = [87, 123, 456, 789, 101112, 131415, 161718, 192021, 222324, 252627]
numerosEmbaralhados = shuffle(numeros)

tipo_ordencao = input("Digite o tipo de ordenação (bubble, quick, counting): ").strip().lower()   
        
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
                
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
    return arr
        
def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    counts = [0] * (max_val + 1)
    
    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        sorted_arr[counts[num] - 1] = num
        counts[num] -= 1

    return sorted_arr

def ordenar_numeros(lista, tipo_ordenacao):
    if tipo_ordenacao == "counting":
        return counting_sort(lista)
    elif tipo_ordenacao == "bubble":
        return bubble_sort(lista)
    elif tipo_ordenacao == "quick":
        return quick_sort(lista, 0, len(lista) - 1)
    
print("Lista embaralhada:", numerosEmbaralhados)
print("Lista ordenada:", ordenar_numeros(numeros, tipo_ordencao))     