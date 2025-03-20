print("|-------------Verificação da Aprovação de Ano-------------|")
nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")

print("")

media = (float(nota1) + float(nota2)) / 2

if media >= 7:
    print(f"Sua media foi {media} e vocé foi aprovado!")
elif media < 7 and media >= 5:
    print(f"Sua media foi {media} e vocé está de recuperação!")
else:
    print(f"Sua media foi {media} e vocé foi reprovado!")