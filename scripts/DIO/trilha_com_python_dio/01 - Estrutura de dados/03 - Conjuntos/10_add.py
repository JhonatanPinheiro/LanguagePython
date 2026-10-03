# Set (conjunto) não permite valores repetidos.
# Se você tentar colocar o mesmo valor várias vezes, ele aparecerá apenas uma vez.

sorteio = {1, 23}  # Cria um conjunto com os números 1 e 23

sorteio.add(25)  # Adiciona o número 25 ao conjunto → {1, 23, 25}
print(sorteio)  # Exibe o conjunto → {1, 23, 25}

sorteio.add(42)  # Adiciona o número 42 ao conjunto → {1, 23, 25, 42}
print(sorteio)  # Exibe o conjunto → {1, 23, 25, 42}

sorteio.add(25)  # Tenta adicionar 25 novamente; 25 já existe, então nada é alterado
print(sorteio)  # Continua com → {1, 23, 25, 42}

# Observação: add() adiciona um único elemento ao set; se o elemento já existir, o set permanece igual.