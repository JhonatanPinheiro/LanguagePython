conjunto_a = {1, 2, 3}  # Cria o conjunto A
conjunto_b = {2, 3, 4}  # Cria o conjunto B

resultado = conjunto_a.difference(conjunto_b)  # Elementos que estão em A, mas não estão em B
print(resultado)  # {1}

resultado = conjunto_b.difference(conjunto_a)  # Elementos que estão em B, mas não estão em A
print(resultado)  # {4}

# Observação: difference() considera o conjunto que está antes do ponto como referência; a ordem altera o resultado.