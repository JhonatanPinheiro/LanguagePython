# Desafio
# Em uma equipe de Engenharia de Dados, voce recebeu a tarefa de validar pequenos lotes de registros antes que eles sigam para o pipeline principal. Cada lote chega como uma sequencia curta de numeros inteiros, e o time quer uma verificacao simples para identificar rapidamente se os dados estao em ordem crescente, decrescente ou sem padrao util. Como o processo faz parte de um treinamento interno com Python em desafios de logica, sua missao e criar um programa enxuto, claro e confiavel.

# Implemente uma solucao que leia exatamente tres numeros inteiros e classifique a ordem em que eles aparecem. Se o primeiro for menor que o segundo e o segundo for menor que o terceiro, imprima CRESCENTE. Se o primeiro for maior que o segundo e o segundo for maior que o terceiro, imprima DECRESCENTE. Em qualquer outro caso, incluindo valores iguais entre si ou apenas parcialmente ordenados, imprima DESORDENADO. O problema deve ser resolvido apenas com comparacoes logicas simples, sem necessidade de estruturas complexas. Cada teste e independente, e a resposta deve considerar somente os tres valores recebidos na entrada atual.

# Entrada
# A entrada contem uma unica linha com tres numeros inteiros separados por espaco. Eles representam a ordem de chegada de tres registros em um lote.

# Saída
# Imprima uma unica palavra, em letras maiusculas: CRESCENTE, DECRESCENTE ou DESORDENADO.

# Exemplos
# A tabela abaixo apresenta exemplos de entrada e saída:

# Entrada	Saída
# 1 2 3	CRESCENTE
# 9 5 1	DECRESCENTE
# 4 4 7	DESORDENADO
# 2 9 3	DESORDENADO

valores = input().split()
primeiro, segundo, terceiro = map(int, valores)

# Verifica se os valores estão em ordem crescente
if primeiro < segundo < terceiro:
    print("CRESCENTE")

# Verifica se os valores estão em ordem decrescente
elif primeiro > segundo > terceiro:
    print("DECRESCENTE")

# Caso não atendam às condições anteriores
else:
    print("DESORDENADO")