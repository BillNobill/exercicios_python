import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados fornecidos
horas_sono = [6.5, 7.0, 5.0, 6.0, 8.0]
copos_cafe = [3, 2, 4, 3, 2]

# Criar o gráfico de dispersão
plt.scatter(horas_sono, copos_cafe, color='purple')  # Pontos na cor roxa

# Adicionar títulos e rótulos
plt.title('Relação entre Horas de Sono e Consumo de Café')
plt.xlabel('Horas de Sono')
plt.ylabel('Copos de Café')

# Exibir grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
