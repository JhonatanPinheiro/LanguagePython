#CONHECENDO METODOS UTEIS DA CLASSE STRING

nome = " Jhonatan Pinheiro "

print(nome.upper()) #Deixa tudo em maiusculos
print(nome.lower()) #Deixa tudo em minusculos
print(nome.title()) #Deixa todas as primeiras letras em maiusculos

print(nome.strip()) #Remove espaço da esquerda e da direita
print(nome.rstrip()) #Remove espaço da direira
print(nome.lstrip()) #Remove espaco da esquerda

print(nome.center(40))
print(nome.center(40,"#")) #Faltando os 40 caracteres para completar será adicionando de forma centralida (esquerdas e direitas) até completar os 40 com #
print("-".join(nome)) #Ira passar por cada letra e irá colocar - logo apos
