contatos = {  # Cria um dicionário de contatos

    "Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"},  # Contato do Jhonatan
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},  # Contato da Giovanna
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},  # Contato do Chappie
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},  # Contato da Melaine

}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # Acessa o contato da Giovanna e depois acessa o telefone

print(telefone)  # Exibe o telefone → "3443-2121"

# Observação: primeiro acessamos a chave "giovanna@gmail.com" e depois, dentro do dicionário encontrado, acessamos a chave "telefone".