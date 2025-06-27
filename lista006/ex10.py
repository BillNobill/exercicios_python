vetor =  [1, 4, 5, 2, 10, 3, 7]

numerosMaioresQueCinco = 0

for numero in vetor:
    if numero > 5:
        numerosMaioresQueCinco += 1
        
print(f"Existem {numerosMaioresQueCinco} números maiores que 5.")