contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria um dicionário com um contato

resultado = contatos.items()  # Retorna as chaves e os valores do dicionário

print(resultado)  # Exibe os pares no formato dict_items([...])

# Observação: items() retorna cada par como (chave, valor), permitindo percorrer os dois juntos em um for.