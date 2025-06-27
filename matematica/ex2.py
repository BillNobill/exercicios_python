import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados fornecidos
temperatura_c = [30, 25, 20, 15, 10]
vendas_sopa = [50, 70, 90, 110, 130]

# Criar o gráfico de dispersão
plt.scatter(temperatura_c, vendas_sopa, color='red')  # Pontos na cor vermelha

# Adicionar títulos e rótulos
plt.title('Relação entre Temperatura e Vendas de Sopa')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Vendas de Sopa')

# Exibir grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
