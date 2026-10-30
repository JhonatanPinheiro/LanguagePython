# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]  # Cria uma lista com números inteiros
pares = [numero for numero in numeros if numero % 2 == 0]  # Filtra e mantém apenas os números pares
print(pares)  # Exibe a lista com os números pares

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]  # Cria uma lista com números inteiros
quadrado = [numero**2 for numero in numeros]  # Cria uma nova lista com cada número elevado ao quadrado
print(quadrado)  # Exibe a lista com os números elevados ao quadrado