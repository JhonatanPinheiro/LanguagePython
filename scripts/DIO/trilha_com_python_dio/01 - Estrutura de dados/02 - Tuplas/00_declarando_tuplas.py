#Tuplas sao estruturas de dados muito parecidas com as listas, a principal diferença é que tuplas são imutáveis enquanto listas são mutáveis. Podemos criar tuplas através da classe tuple, ou colocando valores separados por vírgula de parenteses!
frutas = (                         # Cria uma tupla chamada frutas
    "laranja",                     # Primeiro elemento da tupla
    "pera",                        # Segundo elemento da tupla
    "uva",                         # Terceiro elemento da tupla
)
print(frutas)                      # Exibe a tupla completa


letras = tuple("python")           # Converte cada caractere de "python" em um elemento da tupla
print(letras)                      # Exibe a tupla de letras


# Criando uma tupla a partir de uma string
# Cada caractere da string será um elemento da tupla
nomecompleto = tuple("Jhonatan Pinheiro da Silva")

print(nomecompleto)
# Resultado: ('J', 'h', 'o', 'n', 'a', 't', 'a', 'n', ' ', 'P', 'i', 'n', 'h', 'e', 'i', 'r', 'o', ' ', 'd', 'a', ' ', 'S', 'i', 'l', 'v', 'a')
print(nomecompleto[2])# Acessa o elemento que está no índice 2 # Índices começam em 0 # Resultado: o

print(nomecompleto[2:])
# Fatiamento (slicing) # Começa no índice 2 e vai até o final da tupla
# Resultado: ('o', 'n', 'a', 't', 'a', 'n', ' ', 'P', 'i', 'n', 'h', 'e', 'i', 'r', 'o', ' ', 'd', 'a', ' ', 'S', 'i', 'l', 'v', 'a')

print(nomecompleto[1:3])
# Começa no índice 1 e vai até o índice 3# O índice 3 NÃO é incluído # Resultado: ('h', 'o')

print(nomecompleto[0:3:2])
# Começa no índice 0 # Vai até o índice 3 (sem incluir o 3) # O último número 2 indica o passo: pula de 2 em 2
# Resultado: ('J', 'o')

print(nomecompleto[::])
# Sem início e sem fim # Percorre toda a tupla # Resultado: a tupla completa


print(nomecompleto[::-1])
# Percorre toda a tupla de trás para frente # O passo -1 indica que a leitura será invertida
# Resultado: ('a', 'v', 'l', 'i', 'S', ' ', 'a', 'd', ' ', 'o', 'r', 'i', 'e', 'h', 'n', 'i', 'P', ' ', 'n', 'a', 't', 'a', 'n', 'o', 'h', 'J')

numeros = tuple([1, 2, 3, 4])      # Converte a lista [1, 2, 3, 4] em uma tupla
print(numeros)                     # Exibe a tupla de números


pais = ("Brasil",)                 # Cria uma tupla com apenas um elemento # A vírgula é necessária para indicar que é uma tupla
print(pais)                        # Exibe a tupla

'''''
| Categoria     | Comando              | O que faz                                   | Exemplo              |
| ------------- | -------------------- | ------------------------------------------- | -------------------- |
| **Método**    | `.count()`           | Conta quantas vezes um valor aparece        | `tupla.count("uva")` |
| **Método**    | `.index()`           | Retorna o índice da primeira ocorrência     | `tupla.index("uva")` |
| **Função**    | `len()`              | Retorna a quantidade de elementos           | `len(tupla)`         |
| **Função**    | `min()`              | Retorna o menor valor                       | `min(tupla)`         |
| **Função**    | `max()`              | Retorna o maior valor                       | `max(tupla)`         |
| **Função**    | `sum()`              | Soma os valores                             | `sum(tupla)`         |
| **Função**    | `sorted()`           | Ordena os elementos e retorna uma **lista** | `sorted(tupla)`      |
| **Função**    | `reversed()`         | Percorre os elementos na ordem inversa      | `reversed(tupla)`    |
| **Conversão** | `tuple()`            | Converte outro iterável em tupla            | `tuple(lista)`       |
| **Operador**  | `in`                 | Verifica se um elemento existe              | `"uva" in tupla`     |
| **Operador**  | `not in`             | Verifica se um elemento não existe          | `"uva" not in tupla` |
| **Operador**  | `+`                  | Junta duas tuplas                           | `tupla1 + tupla2`    |
| **Operador**  | `*`                  | Repete uma tupla                            | `tupla * 3`          |
| **Índice**    | `[índice]`           | Acessa um elemento específico               | `tupla[0]`           |
| **Slicing**   | `[início:fim]`       | Obtém uma parte da tupla                    | `tupla[1:3]`         |
| **Slicing**   | `[início:fim:passo]` | Obtém parte da tupla usando um passo        | `tupla[0:5:2]`       |
| **Slicing**   | `[::-1]`             | Inverte a tupla                             | `tupla[::-1]`        |
'''