contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria um dicionário com um contato

resultado = contatos.popitem()  # Remove o último item inserido e retorna uma tupla (chave, valor)
print(resultado)  # Exibe → ('Jhonatan@gmail.com', {'nome': 'Jhonatan', 'telefone': '3333-2221'})

# contatos.popitem()  # KeyError → o dicionário está vazio, pois o item anterior já foi removido