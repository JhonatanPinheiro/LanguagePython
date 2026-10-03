contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria um dicionário com um contato

resultado = contatos.pop("Jhonatan@gmail.com")  # Remove a chave e retorna o valor associado a ela
print(resultado)  # Exibe → {'nome': 'Jhonatan', 'telefone': '3333-2221'}

resultado = contatos.pop("Jhonatan@gmail.com", {})  # Tenta remover a chave; como ela já foi removida, retorna {} como valor padrão
print(resultado)  # Exibe → {}

# Observação: pop() remove uma chave do dicionário e retorna o valor que estava associado a ela; se a chave não existir e houver um valor padrão, retorna esse valor.