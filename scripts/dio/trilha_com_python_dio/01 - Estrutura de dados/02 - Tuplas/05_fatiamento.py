tupla = ("p", "y", "t", "h", "o", "n",)  # Cria uma tupla com as letras de "python"

print(tupla[2:])       # Começa no índice 2 e vai até o final → ("t", "h", "o", "n")
print(tupla[:2])       # Começa do início e vai até o índice 2 (não inclui o 2) → ("p", "y")
print(tupla[1:3])      # Começa no índice 1 e vai até o índice 3 (não inclui o 3) → ("y", "t")
print(tupla[0:3:2])    # Começa no índice 0, vai até o índice 3 e pula de 2 em 2 → ("p", "t")
print(tupla[::])       # Percorre toda a tupla, sem definir início, fim ou passo → ("p", "y", "t", "h", "o", "n")
print(tupla[::-1])     # Percorre a tupla de trás para frente → ("n", "o", "h", "t", "y", "p")