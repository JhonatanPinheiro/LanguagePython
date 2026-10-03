numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}  # Cria um set; valores repetidos são eliminados
print(numeros)  # Exibe os valores únicos do set

numeros.discard(1)  # Remove o número 1 do set
numeros.discard(45)  # Tenta remover 45; como não existe, nada acontece

print(numeros)  # Exibe o set sem o número 1

# Observação: a ordem dos elementos de um set não é garantida.