import numpy as np  # Importa a biblioteca NumPy para trabalhar com arrays
import pandas as pd  # Importa a biblioteca Pandas para trabalhar com tabelas
import matplotlib.pyplot as plt  # Importa o módulo de gráficos do Matplotlib

array = np.array([1, 2, 3, 4, 5])  # Cria um array NumPy com cinco números

print(array)  # Exibe o array no terminal

#---------------------
# Usando pandas
#--------------------
dados = {  # Cria um dicionário com os dados dos alunos
    "nome": ["Ana", "Carlos", "Maria"],  # Chave nome com uma lista de nomes
    "idade": [25, 30, 28]  # Chave idade com uma lista de idades
}

df = pd.DataFrame(dados)  # Converte o dicionário em uma tabela do Pandas
print(df)  # Exibe a tabela no terminal


#-------------------
#Usando matplotlib
#-------------------
x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.plot(x,y)
plt.show()      # Exibe o gráfico na tela