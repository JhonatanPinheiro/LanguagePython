resultado = dict.fromkeys(["nome", "telefone"])  # Cria um dicionário com as chaves "nome" e "telefone"; o valor padrão é None
print(resultado)  # Exibe → {"nome": None, "telefone": None}

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # Cria um dicionário com as mesmas chaves e o valor "vazio" para todas
print(resultado)  # Exibe → {"nome": "vazio", "telefone": "vazio"}

# Observação: fromkeys() cria um dicionário usando as chaves informadas e atribui o mesmo valor para todas elas.