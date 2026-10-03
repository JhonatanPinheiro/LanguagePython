pessoa = {"nome": "Jhonatan", "idade": 28}  # Cria um dicionário usando chaves e valores
print(pessoa)  # Exibe o dicionário → {"nome": "Jhonatan", "idade": 28}

pessoa = dict(nome="Jhonatan", idade=28)  # Cria um dicionário usando a função dict()
print(pessoa)  # Exibe o dicionário → {"nome": "Jhonatan", "idade": 28}

pessoa["telefone"] = "3333-1234"  # Adiciona a chave "telefone" com o valor "3333-1234"
print(pessoa)  # Exibe o dicionário → {"nome": "Jhonatan", "idade": 28, "telefone": "3333-1234"}

# Observação: em um dicionário, cada chave é associada a um valor; se a chave já existir, atribuir um novo valor irá alterá-lo.