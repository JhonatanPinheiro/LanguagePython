# ============================================================
# sort() - Ordenando uma lista
# ============================================================
linguagens = ["python", "js", "c", "java", "csharp"]  # Cria uma lista com linguagens
linguagens.sort()  # Ordena os elementos em ordem crescente (alfabética)
print(linguagens)  # ['c', 'csharp', 'java', 'js', 'python']


# ============================================================
# sort(reverse=True) - Ordem decrescente
# ============================================================
linguagens = ["python", "js", "c", "java", "csharp"]  # Cria novamente a lista original
linguagens.sort(reverse=True)  # Ordena os elementos em ordem decrescente (alfabética inversa)
print(linguagens)  # ['python', 'js', 'java', 'csharp', 'c']


# ============================================================
# sort(key=lambda x: len(x)) - Ordenando pelo tamanho
# ============================================================
linguagens = ["python", "js", "c", "java", "csharp"]  # Cria novamente a lista original
linguagens.sort(key=lambda x: len(x))  # Ordena os elementos pelo número de caracteres
print(linguagens)  # ['c', 'js', 'java', 'python', 'csharp']


# ============================================================
# sort(key=lambda x: len(x), reverse=True) - Maior para menor
# ============================================================
linguagens = ["python", "js", "c", "java", "csharp"]  # Cria novamente a lista original
linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena pelo tamanho, do maior para o menor
print(linguagens)  # ['python', 'csharp', 'java', 'js', 'c']