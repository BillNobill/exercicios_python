import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados fornecidos
horas_estudo = [1.0, 2.0, 3.0, 4.0, 5.0]
nota_prova = [50, 60, 70, 80, 90]

# Criar o gráfico de dispersão
plt.scatter(horas_estudo, nota_prova, color='green')  # Pontos na cor verde

# Adicionar títulos e rótulos
plt.title('Relação entre Horas de Estudo e Nota da Prova')
plt.xlabel('Horas de Estudo')
plt.ylabel('Nota da Prova')

# Exibir grade
plt.grid(True)

# Mostrar o gráfico
plt.show()
