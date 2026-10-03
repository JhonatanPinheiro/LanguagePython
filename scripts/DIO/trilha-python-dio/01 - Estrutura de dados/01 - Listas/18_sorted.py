linguagens = ["python", "js", "c", "java", "csharp"]  # Cria uma lista com 5 linguagens

print(sorted(linguagens, key=lambda x: len(x)))  # Cria uma nova lista ordenada pelo tamanho dos elementos
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # Cria uma nova lista ordenada do maior para o menor