print("|-------------Cáculo de Juros Compostos-------------|")
# Capital Inicial (C)
c = float(input("Digite o capital inicial: "))

# Taxa de Juros (r)
r = float(input("Digite a taxa de juros em %: "))

# Tempo (t)
t = int(input("Digite o número de meses: "))

# Montante Final (M)
m = c * ((1 + r / 100) ** t)

print("")
print(f"O montante final é: {m}")
