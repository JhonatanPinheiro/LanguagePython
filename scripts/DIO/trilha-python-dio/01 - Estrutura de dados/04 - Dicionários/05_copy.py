contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria o dicionário original
copia = contatos.copy()  # Cria uma cópia do dicionário
copia["Jhonatan@gmail.com"] = {"nome": "Gui"}  # Altera o valor da chave na cópia

print(contatos["Jhonatan@gmail.com"])  # Exibe o valor do dicionário original → {"nome": "Jhonatan", "telefone": "3333-2221"}
print(copia["Jhonatan@gmail.com"])  # Exibe o valor da cópia → {"nome": "Gui"}

# Observação: copy() cria uma cópia independente do dicionário principal; alterar a chave na cópia não altera o dicionário original.