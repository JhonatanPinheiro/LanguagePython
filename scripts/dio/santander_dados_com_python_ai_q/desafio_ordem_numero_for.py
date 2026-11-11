# Desafio
# Em uma equipe de Engenharia de Dados, voce recebeu a tarefa de validar pequenos lotes de registros antes que eles sigam para o pipeline principal. Cada lote chega como uma unica linha de texto com valores inteiros separados por espaco. Para evitar retrabalho, a equipe quer uma verificacao simples: descobrir se a sequencia esta em ordem crescente, em ordem decrescente ou desorganizada.

# Implemente um programa que leia a sequencia e classifique o lote. Considere crescente quando cada numero for maior ou igual ao anterior. Considere decrescente quando cada numero for menor ou igual ao anterior. Se nenhuma dessas condicoes for satisfeita, o lote deve ser classificado como misto. Caso a entrada contenha menos de dois numeros, o lote tambem deve ser considerado misto, pois nao ha informacao suficiente para validar uma tendencia. O problema deve ser resolvido apenas com logica basica, comparacoes e repeticao.

# Entrada
# A entrada contem uma unica linha com zero ou mais numeros inteiros separados por um unico espaco. A linha pode representar uma sequencia vazia, um unico valor ou varios valores. Todos os valores devem ser interpretados individualmente na ordem em que aparecem.

# Saída
# Exiba uma unica string. Imprima crescente se a sequencia estiver em ordem crescente, decrescente se estiver em ordem decrescente, ou misto nos demais casos.

# Exemplos
# A tabela abaixo apresenta exemplos de entrada e saída:

# Entrada	Saída
# 1 2 2 5	crescente
# 9 7 7 3	decrescente
# 4 1 6	misto
# 8	misto

linha = input().strip()  # Recebe a entrada e remove espaços extras nas extremidades

if not linha:
    print("misto")  # Se a entrada estiver vazia, classifica como misto
else:
    numeros = [int(valor) for valor in linha.split()]  # Converte os valores para inteiros

    if len(numeros) < 2:
        print("misto")  # Com menos de dois números, não é possível validar a ordem
    else:
        eh_crescente = True  # Considera inicialmente que a sequência é crescente
        eh_decrescente = True  # Considera inicialmente que a sequência é decrescente

        for i in range(1, len(numeros)):
            atual = numeros[i]  # Obtém o número atual
            anterior = numeros[i - 1]  # Obtém o número anterior

            # Se o atual for menor que o anterior, não é crescente
            if atual < anterior:
                eh_crescente = False

            # Se o atual for maior que o anterior, não é decrescente
            if atual > anterior:
                eh_decrescente = False

        if eh_crescente:
            print("crescente")
        elif eh_decrescente:
            print("decrescente")
        else:
            print("misto")