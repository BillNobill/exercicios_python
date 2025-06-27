num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
sinal = input("Digite o sinal da operação (+, -, *, /): ")

def calculadora(num1, num2, sinal):
    if sinal == "+":
        return num1 + num2
    elif sinal == "-":
        return num1 - num2
    elif sinal == "*":
        return num1 * num2
    elif sinal == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Sinal inválido!"
    
resultado = calculadora(num1, num2, sinal)
print(f"O resultado da operação {num1} {sinal} {num2} é: {resultado}")
