numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}  # Cria um set; valores repetidos são eliminados

print(numeros)  # Exibe os valores únicos do set
print(numeros.remove(0))  # Remove o elemento 0, mas NÃO retorna o elemento removido
print(numeros)  # Exibe o set sem o elemento 0

# Observação: remove() não retorna o elemento removido. Por isso, print(numeros.remove(0)) exibe None.