def exibir_mensagem():  # Define uma função sem parâmetros
    print("Olá mundo!")  # Exibe uma mensagem na tela


def exibir_mensagem_2(nome):  # Define uma função que recebe o parâmetro nome
    print(f"Seja bem vindo {nome}!")  # Exibe a mensagem usando o nome recebido


def exibir_mensagem_3(nome="Anônimo"):  # Define uma função com parâmetro padrão "Anônimo"
    print(f"Seja bem vindo {nome}!")  # Exibe a mensagem usando o nome recebido


exibir_mensagem()  # Chama a função sem precisar passar nenhum argumento

exibir_mensagem_2(nome="Jhonatan")  # Chama a função passando "Jhonatan" para o parâmetro nome

exibir_mensagem_3()  # Chama a função sem argumento; usa o valor padrão "Anônimo"

exibir_mensagem_3(nome="Chappie")  # Chama a função passando "Chappie"; substitui o valor padrão

# Observação: parâmetros são definidos na função; argumentos são os valores passados quando chamamos a função.