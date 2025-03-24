print("|-------------Cálculo de Juros Simples-------------|")
# Capital Inicial (C)
c = float(input("Digite o capital inicial: "))

# Taxa de Juros (r)
i = float(input("Digite a taxa de juros em %: "))

# Tempo (t)
t = int(input("Digite o número de meses: "))

# Montante Final (M)
m = c + (c * (i / 100) * t)

print("")

print(f"O montante final é: {m}")
