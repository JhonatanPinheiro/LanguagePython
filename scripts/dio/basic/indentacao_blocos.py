saldo = 500
def sacar(valor: float):
    global saldo

    if saldo >= valor:
        print("Saldo Disponível:", saldo)
        print("Valor Sacado:", valor)

        saldo = saldo - valor

        print("Total de Saldo Disponível:", saldo)
        print("-" * 30)
    else:
        print("Saldo insuficiente!")


sacar(100)
sacar(100)
sacar(100)
sacar(100)