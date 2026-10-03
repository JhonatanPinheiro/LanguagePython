def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):  # Antes de / = somente posição; depois de * = somente nome

    print(modelo, ano, placa, marca, motor, combustivel)  # Exibe os valores recebidos


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Correto: primeiros parâmetros por posição e últimos por nome
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # Inválido: modelo, ano e placa são somente posicionais

# Observação: "/" torna os parâmetros anteriores somente posicionais; "*" torna os parâmetros seguintes somente nomeados.