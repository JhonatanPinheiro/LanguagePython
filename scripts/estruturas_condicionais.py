MAIOR_IDADE = 18
IDADE_ESPECIAL = 80

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE and idade < IDADE_ESPECIAL:
    print("Maior de idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Está na idade especial, não pode tirar CNH")

else:
    print("Ainda não pode tirar a CNH")