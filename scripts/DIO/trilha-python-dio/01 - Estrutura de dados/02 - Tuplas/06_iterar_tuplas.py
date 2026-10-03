carros = (                         # Cria uma tupla com 3 carros
    "gol",                         # Primeiro carro
    "celta",                       # Segundo carro
    "palio",                       # Terceiro carro
)

for carro in carros:               # Percorre cada carro da tupla
    print(carro)                   # Exibe o carro atual


for indice, carro in enumerate(carros):  # Percorre a tupla pegando índice e valor
    print(f"{indice}: {carro}")          # Exibe o índice e o carro