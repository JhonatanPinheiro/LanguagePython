def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):  # modelo, ano e placa só podem ser passados por posição; os demais podem ser por nome

    print(modelo, ano, placa, marca, motor, combustivel)  # Exibe os valores recebidos


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Correto: os 3 primeiros são posicionais e os demais são nomeados
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Inválido: modelo, ano e placa não podem ser passados por nome

# Observação: "/" determina que os parâmetros à esquerda dele são somente posicionais; os parâmetros à direita podem ser posicionais ou nomeados.