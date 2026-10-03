contatos = {  # Cria um dicionário com vários contatos
    "Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"},  # Primeiro contato
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},  # Segundo contato
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},  # Terceiro contato
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},  # Quarto contato
}

resultado = "Jhonatan@gmail.com" in contatos  # Verifica se essa chave existe no dicionário → True
print(resultado)  # Exibe → True

resultado = "megui@gmail.com" in contatos  # Verifica se essa chave existe no dicionário → False
print(resultado)  # Exibe → False

resultado = "idade" in contatos["Jhonatan@gmail.com"]  # Verifica se "idade" existe dentro do contato do Jhonatan → False
print(resultado)  # Exibe → False

resultado = "telefone" in contatos["giovanna@gmail.com"]  # Verifica se "telefone" existe dentro do contato da Giovanna → True
print(resultado)  # Exibe → True

# Observação: quando usamos "in" em um dicionário, por padrão verificamos se a chave existe, e não se o valor existe.