# Funcao de Somar

def somar(a, b):  # Define uma função que recebe dois números
    return a + b  # Soma os dois números e retorna o resultado


# Funcao de Subtracao

def subtrair(a, b):  # Define uma função que recebe dois números
    return a - b  # Subtrai os dois números e retorna o resultado


# Funcao de Multiplicacao

def multiplicacao(a, b):  # Define uma função que recebe dois números
    return a * b  # Multiplica os dois números e retorna o resultado


# Funcao de Divisão

def divisao(a, b):  # Define uma função que recebe dois números
    return a / b  # Divide os dois números e retorna o resultado


# Funcao para Exibir o Resultado

def exibir_resultado(a, b, funcao):  # Define uma função que recebe dois números e outra função
    resultado = funcao(a, b)  # Executa a função recebida passando a e b como argumentos
    print(f"O resultado da operação {a} + {b} = {resultado}")  # Exibe o resultado da operação


exibir_resultado(10, 10, somar)  # Passa 10, 10 e a função somar → 10 + 10 = 20

exibir_resultado(10, 10, subtrair)  # Passa 10, 10 e a função subtrair → 10 - 10 = 0

exibir_resultado(10, 10, multiplicacao)  # Passa 10, 10 e a função multiplicacao → 10 * 10 = 100

exibir_resultado(10, 10, divisao)  # Passa 10, 10 e a função divisao → 10 / 10 = 1


# Atribuindo a funcao para uma variavel

variavel_exibir_resultado = exibir_resultado  # A variável agora aponta para a função exibir_resultado

print(variavel_exibir_resultado(4, 24, multiplicacao))  # Executa a função através da variável

# Observação: em Python, funções podem ser armazenadas em variáveis e também passadas como argumentos para outras funções.