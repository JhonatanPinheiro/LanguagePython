matriz = (                         # Cria uma tupla contendo outras tuplas
    (1, "a", 2),                   # Primeira tupla / linha
    ("b", 3, 4),                   # Segunda tupla / linha
    (6, 5, "c"),                   # Terceira tupla / linha
)

print(matriz[0])                   # Acessa a primeira tupla → (1, "a", 2)
print(matriz[0][0])                # Acessa a primeira tupla e o primeiro elemento → 1
print(matriz[0][-1])               # Acessa a primeira tupla e o último elemento → 2
print(matriz[-1][-1])              # Acessa a última tupla e o último elemento → "c"