# ============================================================
# INTERPOLAÇÃO DE VARIÁVEIS
# ============================================================


# Método .format() — argumentos nomeados

nome = "Jhonatan"
idade = 28
profissao = "Cientista de Dados"
linguagem = "Python"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(
    nome=nome,              # {nome} recebe o valor da variável nome
    idade=idade,            # {idade} recebe o valor da variável idade
    profissao=profissao,    # {profissao} recebe o valor da variável profissao
    linguagem=linguagem     # {linguagem} recebe o valor da variável linguagem
))


# .format() com dicionário

pessoa = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa))  # ** desempacota o dicionário


# .format() — argumentos posicionais

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(
    nome,          # Primeiro {} → nome
    idade,         # Segundo {} → idade
    profissao,     # Terceiro {} → profissao
    linguagem      # Quarto {} → linguagem
))


# .format() — argumentos por índice

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(
    linguagem,     # {0} → linguagem
    profissao,     # {1} → profissao
    idade,         # {2} → idade
    nome           # {3} → nome
))


# Operador % — forma antiga de interpolação

nome = "Jhonatan Pinheiro"
idade = 28
profissao = "Analista de Dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (
    nome,          # %s → string
    idade,         # %d → número inteiro
    profissao,     # %s → string
    linguagem      # %s → string
))


# F-String — forma moderna e mais utilizada

nome = "Jhonatan"
idade = 28
profissao = "Cientista de Dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")  # f permite inserir variáveis diretamente dentro de {}


# ============================================================
# RESUMO
# ============================================================

# %              → forma antiga / código legado
# .format()      → forma intermediária / ainda encontrada
# f-string       → forma moderna / mais utilizada atualmente