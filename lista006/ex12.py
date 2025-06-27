lista =  [3, 5, 9, 12, 17, 18, 20]

somatoriaMultiplos = 0

for numero in lista:
    if numero % 3 == 0:
        print(f"{numero} é um multiplo de 3.")
        somatoriaMultiplos += numero
        
print(f"A somatória dos múltiplos de 3 é: {somatoriaMultiplos}.")