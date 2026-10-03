conjunto_a = {1, 2, 3}  # Cria o conjunto A
conjunto_b = {4, 1, 2, 5, 6, 3}  # Cria o conjunto B

resultado = conjunto_a.issubset(conjunto_b)  # Verifica se todos os elementos de A estão em B → True
print(resultado)  # True

resultado = conjunto_b.issubset(conjunto_a)  # Verifica se todos os elementos de B estão em A → False
print(resultado)  # False

# Observação: issubset() verifica se o conjunto da esquerda está totalmente contido no conjunto da direita.