carros = {"gol", "celta", "palio"}  # Cria um set com 3 carros
                                    # Elementos não possuem ordem garantida

for carro in carros:  # Percorre cada carro do set
    print(carro)  # Exibe o carro atual


for indice, carro in enumerate(carros):  # Percorre o set e gera contador + valor
    print(f"{indice}: {carro}")  # Exibe o contador e o carro

# Observação: enumerate() cria um contador durante a iteração, mas o set continua sem ordem garantida.