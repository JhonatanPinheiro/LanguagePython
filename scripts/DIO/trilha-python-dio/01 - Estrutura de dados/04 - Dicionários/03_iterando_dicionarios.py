contatos = {  # Cria um dicionário com os contatos
    "Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"},  # Contato do Jhonatan
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},  # Contato da Giovanna
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},  # Contato do Chappie
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},  # Contato da Melaine
}

for chave in contatos:  # Percorre o dicionário; por padrão, percorre as chaves
    print(chave, contatos[chave])  # Exibe a chave e acessa o valor usando a chave

print("=" * 100)  # Exibe uma linha com 100 sinais de igual

for chave, valor in contatos.items():  # Percorre o dicionário obtendo chave e valor ao mesmo tempo
    print(chave, valor)  # Exibe a chave e o valor

# Observação: for chave in contatos percorre as chaves; items() permite receber chave e valor diretamente.