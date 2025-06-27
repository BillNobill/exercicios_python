texto = input("Digite um texto: ")

vogais = "aeiouAEIOU"

def contar_vogais(texto):
    quantidadeVogais = 0
    for letra in texto:
        if letra in vogais:
            quantidadeVogais += 1
    return quantidadeVogais

print("A quantidade de vogais é: " + str(contar_vogais(texto)))