carros = ["gol", "celta", "palio"]  # Cria uma lista com três elementos do tipo string

for carro in carros:  # Percorre cada elemento da lista e armazena o valor na variável "carro"
    print(carro)  # Exibe o valor atual da variável "carro"


for indice, carro in enumerate(carros):  # Percorre a lista obtendo o índice e o valor de cada elemento
    print(f"{indice}: {carro}")  # Exibe o índice e o valor do elemento