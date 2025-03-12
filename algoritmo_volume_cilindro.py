from math import pi

print("|-------------Cálculo do Volume do Cilindro-------------|")
# Raio (r)
r = float(input("Digite o raio do cilindro: "))
# Altura (h)
h = float(input("Digite a altura do cilindro: "))

# Área da base (A)
a = pi * (r * r)

# Volume (V)
v = a * h

print("")
print(f"O volume do seu cilindro é: {v:.2f}")
