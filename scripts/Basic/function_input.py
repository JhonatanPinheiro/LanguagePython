nome = 'Jhonatan'
sobrenome = 'Pinheiro'

print(nome,sobrenome)
print(nome,sobrenome,end="...\n")
print(nome,sobrenome, sep="#")

nome_completo = input('Informe seu Nome Completo: ')

concatencacao_nome_sobrenome = (nome+" "+sobrenome)
print(concatencacao_nome_sobrenome)

print("Nome no Input pelo Usuário: ", nome_completo)
print("Nome Concatenado pelo Usuário do Sistema", concatencacao_nome_sobrenome)

resultado = ''

if nome_completo == concatencacao_nome_sobrenome:
    resultado = True
else:
    resultado = False

print(resultado)