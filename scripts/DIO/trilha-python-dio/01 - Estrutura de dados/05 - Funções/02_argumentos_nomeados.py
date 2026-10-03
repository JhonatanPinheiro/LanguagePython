def salvar_carro(marca, modelo, ano, placa):  # Define uma função com 4 parâmetros obrigatórios

    # salva carro no banco de dados...  # Comentário: representaria o salvamento do carro

    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")  # Exibe os dados do carro


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")  # Passa os argumentos pela posição
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")  # Passa os argumentos pelo nome dos parâmetros
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})  # Desempacota o dicionário e passa cada chave como argumento

# Observação: as três chamadas fazem a mesma coisa; o que muda é a forma como os argumentos são enviados para a função.