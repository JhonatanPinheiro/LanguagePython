conjunto_a = {1, 2, 3}  # Cria o conjunto A
conjunto_b = {2, 3, 4}  # Cria o conjunto B

resultado = conjunto_a.symmetric_difference(conjunto_b)  # Pega os elementos que não são comuns aos dois conjuntos
print(resultado)  # {1, 4}

# Observação: symmetric_difference() retorna os elementos que estão em A ou em B, mas não nos dois ao mesmo tempo.