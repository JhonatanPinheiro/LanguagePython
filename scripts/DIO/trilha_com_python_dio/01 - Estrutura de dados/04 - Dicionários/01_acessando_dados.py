dados = {"nome": "Jhonatan", "idade": 28, "telefone": "3333-1234"}  # Cria um dicionário com chave e valor

print(dados["nome"])  # Acessa o valor da chave "nome" → "Jhonatan"
print(dados["idade"])  # Acessa o valor da chave "idade" → 28
print(dados["telefone"])  # Acessa o valor da chave "telefone" → "3333-1234"

dados["nome"] = "Maria"  # Altera o valor da chave "nome"

dados["idade"] = 18  # Altera o valor da chave "idade"

dados["telefone"] = "9988-1781"  # Altera o valor da chave "telefone"

print(dados)  # Exibe o dicionário atualizado → {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

# Observação: para acessar ou alterar um valor, usamos a chave entre colchetes []; se a chave já existe, o valor é atualizado.