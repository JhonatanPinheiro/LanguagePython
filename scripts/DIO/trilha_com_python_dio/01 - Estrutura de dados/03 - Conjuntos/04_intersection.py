conjunto_a = {1, 2, 3}  # Cria o primeiro conjunto
conjunto_b = {2, 3, 4}  # Cria o segundo conjunto

resultado = conjunto_a.intersection(conjunto_b)  # Encontra os elementos em comum

print(resultado)  # {2, 3}

# Observação: intersection() não altera os conjuntos originais; ele retorna um novo conjunto com os elementos em comum.