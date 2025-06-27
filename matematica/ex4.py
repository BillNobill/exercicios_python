import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados fornecidos
tamanho_sapato = [38, 40, 42, 36, 44]
nota_matematica = [70, 55, 90, 65, 75]

# Criar o gráfico de dispersão
plt.scatter(tamanho_sapato, nota_matematica, color='brown')  # Pontos na cor marrom

# Adicionar títulos e rótulos
plt.title('Tamanho do Sapato vs Nota em Matemática')
plt.xlabel('Tamanho do Sapato')
plt.ylabel('Nota em Matemática')

# Exibir grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
