conjunto_a = {1, 2, 3}  # Cria o conjunto A
conjunto_b = {4, 1, 2, 5, 6, 3}  # Cria o conjunto B

resultado = conjunto_a.issuperset(conjunto_b)  # Verifica se A contém todos os elementos de B → False
print(resultado)  # False

resultado = conjunto_b.issuperset(conjunto_a)  # Verifica se B contém todos os elementos de A → True
print(resultado)  # True

# Observação: issuperset() verifica se o conjunto da esquerda contém todos os elementos do conjunto da direita.