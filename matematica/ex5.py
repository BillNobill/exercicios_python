import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados fornecidos
estresse = [1, 2, 3, 4, 5]
desempenho = [60, 70, 80, 75, 60]

# Criar o gráfico de dispersão
plt.scatter(estresse, desempenho, color='orange')  # Pontos na cor laranja

# Adicionar títulos e rótulos
plt.title('Relação entre Estresse e Desempenho')
plt.xlabel('Nível de Estresse')
plt.ylabel('Desempenho')

# Exibir grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
