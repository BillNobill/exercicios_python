nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))

media = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4

if media >= 7:
    print(f"A média é {media}, o aluno foi aprovado.")
else:
    print(f"A média é {media}, o aluno foi reprovado.")