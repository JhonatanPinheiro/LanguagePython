contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria um dicionário com um contato

contatos.update({"Jhonatan@gmail.com": {"nome": "Jhow"}})  # Atualiza a chave existente e substitui todo o valor anterior
print(contatos)  # Exibe → {'Jhonatan@gmail.com': {'nome': 'Jhow'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})  # Adiciona uma nova chave ao dicionário
print(contatos)  # Exibe → {'Jhonatan@gmail.com': {'nome': 'Jhow'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

# Observação: update() altera uma chave existente ou adiciona uma nova; quando a chave já existe, o valor antigo é substituído pelo novo.