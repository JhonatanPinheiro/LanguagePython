#Loop Infinito com While
while True:

    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)
    
""""
## Comando While
opcao = -1

while opcao != 0:
    opcao = int(input(" [1] Sacar\n [2] Extrato\n [0] Sair\n: "))

    if opcao == 1:
        print("Sacando")
    elif opcao == 2:
        print("Exibindo o extrato")
    else:
        print("Deslogado do Sistema")
"""

"""
## Exemplo com funcao Range e a (Comando de funcao built -in range)
for numero in range(0,100,20):
    print(numero, end=" ")

"""

"""
## Exemplo com for/else  (Comando  for )
texto = input("Informe um texto: ")

VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra,end="")
else:
    print('')
    print("Executa no final do laço")

"""