contatos = {  # Cria um dicionário com vários contatos
    "Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"},  # Primeiro contato
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},  # Segundo contato
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},  # Terceiro contato
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},  # Quarto contato
}

del contatos["Jhonatan@gmail.com"]["telefone"]  # Remove somente a chave "telefone" do contato do Jhonatan

del contatos["chappie@gmail.com"]  # Remove completamente o contato do Chappie

print(contatos)  # Exibe o dicionário depois das duas remoções

# Observação: del pode remover uma chave específica ou um elemento inteiro do dicionário; também pode acessar dicionários aninhados.