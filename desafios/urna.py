print("Urna eletrônica!")
cpf = ""
davi = 0
arthur = 0

while (cpf != "Terminar votação"):
    cpf = input("Digite seu CPF:")
    if (cpf != "" and cpf != "Terminar votação"):
        candiddatoEscolhido = input("Digite o seu candidato: 1 - Davi, 2 - Arthur: ")
        
        if (candiddatoEscolhido == "1"):
            davi += 1
            print("Seu voto foi confirmado!")
        elif (candiddatoEscolhido == "2"):
            arthur += 1
            print("Seu voto foi confirmado!")
        else: 
            print("Digite um candidato válido!")

    else:
        print("Você não digitou seu CPF!")
        
print("Resultado da votação:")
print("Davi:", davi)
print("Arthu: " + str(arthur))

somaTotal = davi + arthur
print(f"Soma total dos votos: {somaTotal}")

if (davi > arthur):
    print("O vencedor da eleição foi Davi!")
elif (arthur > davi):
    print("O vencedor da eleição foi Arthur!")
else:
    print("A votação empatou!")