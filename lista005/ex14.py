lista = []

for i in range(5):
    lista.append(int(input("Digite um número entre 0 e 10: ")))
    
print("Os números em ordem crescente são:")

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

lista = counting_sort(lista)
print(lista)