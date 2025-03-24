print("|-------------Conversão do Tempo-------------|")
minutos = input("Insira um valor em minutos: ")

print("")

horas = round(float(minutos) / 60, 0)
minutosRestantes = float(minutos) % 60

print(f"{minutos} minutos são {horas} hora(s) e {minutosRestantes} minuto(s)!")