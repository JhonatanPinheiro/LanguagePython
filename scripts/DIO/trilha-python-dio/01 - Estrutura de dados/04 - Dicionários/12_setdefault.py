contato = {"nome": "Jhonatan", "telefone": "3333-2221"}  # Cria um dicionário com nome e telefone

contato.setdefault("nome", "Giovanna")  # "nome" já existe, então mantém "Jhonatan" e não altera o valor
print(contato)  # Exibe → {'nome': 'Jhonatan', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # "idade" não existe, então adiciona a chave com o valor 28
print(contato)  # Exibe → {'nome': 'Jhonatan', 'telefone': '3333-2221', 'idade': 28}

# Observação: setdefault() adiciona a chave somente se ela ainda não existir; se a chave já existir, mantém o valor atual.