contatos = {"Jhonatan@gmail.com": {"nome": "Jhonatan", "telefone": "3333-2221"}}  # Cria um dicionário com um contato

# contatos["chave"]  # KeyError → acessar uma chave que não existe gera um erro

resultado = contatos.get("chave")  # Tenta acessar "chave"; como não existe, retorna None
print(resultado)  # Exibe → None

resultado = contatos.get("chave", {})  # Tenta acessar "chave"; se não existir, retorna {} como valor padrão
print(resultado)  # Exibe → {}

resultado = contatos.get("Jhonatan@gmail.com", {})  # Acessa a chave existente; retorna os dados do Jhonatan
print(resultado)  # Exibe → {"nome": "Jhonatan", "telefone": "3333-2221"}

# Observação: get() evita o KeyError quando a chave não existe e permite definir um valor padrão para essa situação.