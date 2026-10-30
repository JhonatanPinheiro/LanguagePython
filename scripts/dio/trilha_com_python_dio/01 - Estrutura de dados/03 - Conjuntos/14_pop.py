numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}  # Cria um set; valores repetidos são eliminados

print(numeros)  # Exibe os valores únicos do set
print(numeros.pop())  # Remove e retorna um elemento do set
print(numeros.pop())  # Remove e retorna outro elemento do set
print(numeros)  # Exibe os elementos que permaneceram

# Observação: pop() remove um elemento do set, mas a ordem não é garantida; portanto, não sabemos qual elemento será removido.