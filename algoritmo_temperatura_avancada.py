print("|-------------Converter Temperatura-------------|")
temperaturaCelcius = int(input("Digite a temperatura em graus Celcius: "))

# Calculo de temperatura Kelvin
temperaturaKelvin = temperaturaCelcius + 273.15

# Calculo de temperatura Fahrenheit
temperaturaFahrenheit = (temperaturaCelcius * 9 / 5 ) + 32

# Calculo de temperatura Rankine
temperaturaRankine = (temperaturaCelcius + 273.15) * 9 / 5

print("")
print(f"Temperatura em Kelvin: {temperaturaKelvin:.2f}")
print(f"Temperatura em Fahrenheit: {temperaturaFahrenheit:.2f}")
print(f"Temperatura em Rankine: {temperaturaRankine:.2f}")
