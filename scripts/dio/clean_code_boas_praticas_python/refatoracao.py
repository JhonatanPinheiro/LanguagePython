def processar(lista):
    resultado = []
    for i in lista:
        if i > 10:
            resultado.append(i * 2)
    return resultado # retorna somente depois de percorrer toda a lista

#Refatoracao do código a cima!
def processar_numero(lista):
    return [numero * 2 for numero in lista if numero > 10]

# print(processar([50,22]))
# print(processar_numero([50,15,30,1]))