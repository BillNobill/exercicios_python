print("|-------------Verificação do Tipo de Triângulo-------------|")
ladoTriangulo1 = input("Digite o primeiro lado do triângulo: ")
ladoTriangulo2 = input("Digite o segundo lado do triângulo: ")
ladoTriangulo3 = input("Digite o terceiro lado do triângulo: ")

print("")

if ladoTriangulo1 == ladoTriangulo2 == ladoTriangulo3:
    print("O triângulo é Equilátero")
elif ladoTriangulo1 == ladoTriangulo2 or ladoTriangulo1 == ladoTriangulo3 or ladoTriangulo2 == ladoTriangulo3:
    print("O triângulo é Isóceles")
else:
    print("O triângulo é Escaleno")

