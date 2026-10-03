contatos = {  # Cria um dicionário com vários contatos
    "Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"},  # Primeiro contato
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},  # Segundo contato
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},  # Terceiro contato
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},  # Quarto contato
}

resultado = (  # Armazena o resultado em uma variável
    contatos.values()  # Retorna somente os valores do dicionário
)

print(resultado)  # Exibe todos os valores no formato dict_values([...])

# Observação: values() retorna somente os valores, ignorando as chaves do dicionário.