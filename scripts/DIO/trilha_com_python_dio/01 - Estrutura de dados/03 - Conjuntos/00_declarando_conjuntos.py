numeros = set([1, 2, 3, 1, 3, 4])  # Cria um conjunto a partir de uma lista # Valores repetidos são eliminados
print(numeros)  # {1, 2, 3, 4} → os números repetidos foram removidos

letras = set("abacaxi")  # Cria um conjunto a partir de uma string  # Cada caractere repetido é eliminado
print(letras)  # {"b", "a", "c", "x", "i"} → "a" repetido aparece apenas uma vez

carros = set(("palio", "gol", "celta", "palio"))  # Cria um conjunto a partir de uma tupla # "palio" repetido é eliminado
print(carros)  # {"gol", "celta", "palio"} → cada carro aparece apenas uma vez

# Observação: sets não garantem uma ordem fixa dos elementos; a ordem exibida pode variar.