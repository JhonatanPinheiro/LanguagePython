def calcular_total(numeros):  # Define uma função que recebe uma lista de números
    return sum(numeros)  # Soma todos os números e retorna o resultado


def retorna_antecessor_e_sucessor(numero):  # Define uma função que recebe um número
    antecessor = numero - 1  # Calcula o número anterior
    sucessor = numero + 1  # Calcula o número seguinte
    return antecessor, sucessor  # Retorna os dois valores como uma tupla


def func_3():  # Define uma função sem parâmetros
    print('Hello Jhow')  # Exibe a mensagem na tela


print(calcular_total([10, 20, 34]))  # Chama a função e exibe → 64

print(retorna_antecessor_e_sucessor(10))  # Chama a função e exibe → (9, 11)

print(func_3())  # Executa func_3(), exibe "Hello Jhow" e depois exibe None

# Observação: uma função pode retornar mais de um valor; nesse caso, Python retorna os valores agrupados em uma tupla.