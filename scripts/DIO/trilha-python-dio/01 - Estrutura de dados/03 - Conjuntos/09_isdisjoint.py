conjunto_a = {1, 2, 3, 4, 5}  # Cria o conjunto A
conjunto_b = {6, 7, 8, 9}  # Cria o conjunto B
conjunto_c = {1, 0}  # Cria o conjunto C

resultado = conjunto_a.isdisjoint(conjunto_b)  # Verifica se A e B não possuem elementos em comum → True
print(resultado)  # True

resultado = conjunto_a.isdisjoint(conjunto_c)  # Verifica se A e C não possuem elementos em comum → False
print(resultado)  # False

# Observação: isdisjoint() retorna True quando os conjuntos não possuem nenhum elemento em comum.