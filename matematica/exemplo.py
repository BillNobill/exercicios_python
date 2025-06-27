import matplotlib.pyplot as plt  # Importa a biblioteca

# Dados simples com um outlier
# Definimos os valores para os eixos x e y
x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 4, 6, 8, 10, 12, 50]  # 50 é um outlier

# Criar o gráfico de dispersão
plt.scatter(x, y, color='green')  # Plota os pontos com cor azul
plt.title('Gráfico de Dispersão com Outlier')  # Título do gráfico
plt.xlabel('Eixo X')  # Rótulo do eixo X
plt.ylabel('Eixo Y')  # Rótulo do eixo Y
plt.grid(True)  # Exibe a grade no fundo
plt.show()
