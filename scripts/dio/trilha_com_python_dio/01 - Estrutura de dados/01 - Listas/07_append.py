lista = []  # Cria uma lista vazia

lista.append(1)  # Adiciona o número 1 ao final da lista
lista.append("Python")  # Adiciona a string "Python" ao final da lista
lista.append([40, 30, 20])  # Adiciona uma nova lista como elemento da lista principal
lista.append("Jhonatan")

print(lista)  # Exibe a lista completa: [1, "Python", [40, 30, 20]]

#Removendo todas as vogais do ultimo elemento da lista
print(lista[3].translate(str.maketrans("", "", "aiou")))
# Mostrando a lista completa, mas removendo as vogais apenas do último elemento na visualização
print(lista[:3] + [lista[3].translate(str.maketrans("", "", "aiou"))])


'''
| Método      | O que faz                         | Exemplo                  |
| ----------- | --------------------------------- | ------------------------ |
| `append()`  | Adiciona **um** elemento no final | `lista.append(10)`       |
| `insert()`  | Adiciona elemento em uma posição  | `lista.insert(1, 10)`    |
| `extend()`  | Adiciona **vários** elementos     | `lista.extend([10, 20])` |
| `remove()`  | Remove pelo **valor**             | `lista.remove(10)`       |
| `pop()`     | Remove pelo **índice**            | `lista.pop(0)`           |
| `clear()`   | Remove todos os elementos         | `lista.clear()`          |
| `index()`   | Encontra o índice de um valor     | `lista.index(10)`        |
| `count()`   | Conta ocorrências de um valor     | `lista.count(10)`        |
| `sort()`    | Ordena a lista                    | `lista.sort()`           |
| `reverse()` | Inverte a lista                   | `lista.reverse()`        |
| `copy()`    | Cria uma cópia da lista           | `lista.copy()`           |
'''


# ============================================================
# MÉTODOS DE LISTA MAIS IMPORTANTES EM PYTHON
# ============================================================

lista = [10, 20, 30, 40]

# ------------------------------------------------------------
# append()
# ------------------------------------------------------------
lista.append(50)  # Adiciona um elemento no final da lista
print(lista)  # [10, 20, 30, 40, 50]

# ------------------------------------------------------------
# insert()
# ------------------------------------------------------------
lista.insert(1, 15)  # Adiciona o valor 15 na posição de índice 1
print(lista)  # [10, 15, 20, 30, 40, 50]

# ------------------------------------------------------------
# extend()
# ------------------------------------------------------------
lista.extend([60, 70, 80])  # Adiciona vários elementos ao final da lista
print(lista)  # [10, 15, 20, 30, 40, 50, 60, 70, 80]

# ------------------------------------------------------------
# remove()
# ------------------------------------------------------------
lista.remove(30)  # Remove a primeira ocorrência do valor 30
print(lista)  # [10, 15, 20, 40, 50, 60, 70, 80]

# ------------------------------------------------------------
# pop()
# ------------------------------------------------------------
lista.pop()  # Remove e retorna o último elemento da lista
print(lista)  # [10, 15, 20, 40, 50, 60, 70]
lista.pop(1)  # Remove e retorna o elemento do índice 1
print(lista)  # [10, 20, 40, 50, 60, 70]


# ------------------------------------------------------------
# clear()
# ------------------------------------------------------------
lista.clear()  # Remove todos os elementos da lista
print(lista)  # []


# ------------------------------------------------------------
# index()
# ------------------------------------------------------------
lista = [10, 20, 30, 20, 40]
print(lista.index(30))  # Retorna o índice onde o valor 30 está localizado


# ------------------------------------------------------------
# count()
# ------------------------------------------------------------
print(lista.count(20))  # Conta quantas vezes o valor 20 aparece na lista


# ------------------------------------------------------------
# sort()
# ------------------------------------------------------------
lista.sort()  # Ordena a lista em ordem crescente
print(lista)  # [10, 20, 20, 30, 40]


# ------------------------------------------------------------
# reverse()
# ------------------------------------------------------------
lista.reverse()  # Inverte a ordem dos elementos da lista
print(lista)  # [40, 30, 20, 20, 10]


# ------------------------------------------------------------
# copy()
# ------------------------------------------------------------
nova_lista = lista.copy()  # Cria uma cópia independente da lista
print(nova_lista)  # Exibe a cópia da lista