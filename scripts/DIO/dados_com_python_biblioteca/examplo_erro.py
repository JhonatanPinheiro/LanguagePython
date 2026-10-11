# 1. ZeroDivisionError
try:
    # Tenta dividir por zero
    numero = 10 / 0

except ZeroDivisionError:
    # Trata o erro de divisão por zero
    print("Erro: não é possível dividir por zero.")


# 2. ValueError
try:
    # Tenta converter um texto inválido para inteiro
    numero = int("abc")

except ValueError:
    # Trata o erro de valor inválido
    print("Erro: o valor informado não é válido.")


# 3. TypeError
try:
    # Tenta somar tipos diferentes
    resultado = "10" + 5

except TypeError:
    # Trata o erro de tipos incompatíveis
    print("Erro: os tipos são incompatíveis.")


# 4. IndexError
try:
    # Cria uma lista
    lista = [10, 20, 30]

    # Tenta acessar uma posição que não existe
    print(lista[10])

except IndexError:
    # Trata o índice inexistente
    print("Erro: o índice não existe na lista.")
    
#Blocos Try-Except e Finally
try:
    numero = int("10")
    print(numero)
except ValueError:
    print("Erro de conversao");
finally:
    print("Execucao finalizada!")

