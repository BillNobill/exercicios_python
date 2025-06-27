nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

if nota1 >= 7 or nota2 >= 7 or nota1 + nota2 >= 12:
    print("Aprovado")
else:
    print("Reprovado")
    