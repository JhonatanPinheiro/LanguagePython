class Cachorro:  # Define uma classe chamada Cachorro

    def __init__(self, nome, cor, acordado=True):  # Método construtor, executado automaticamente ao criar uma instância
        print("Inicializando a classe...")  # Exibe uma mensagem quando a instância é criada
        self.nome = nome  # Cria o atributo nome
        self.cor = cor  # Cria o atributo cor
        self.acordado = acordado  # Cria o atributo acordado

    def __del__(self):  # Método especial relacionado à destruição da instância
        print("Removendo a instância da classe.")  # Exibe uma mensagem quando a instância é removida

    def falar(self):  # Define o método falar
        print("auau")  # Exibe o som do cachorro


def criar_cachorro():  # Define uma função chamada criar_cachorro
    c = Cachorro("Zeus", "Branco e preto", False)  # Cria uma instância da classe Cachorro
    print(c.nome)  # Exibe o nome do cachorro


c = Cachorro("Chappie", "amarelo")  # Cria uma instância da classe Cachorro

c.falar()  # Chama o método falar da instância c

print("Ola mundo")  # Exibe "Ola mundo" na tela

del c  # Remove a referência da variável c

print("Ola mundo")  # Exibe "Ola mundo" na tela

print("Ola mundo")  # Exibe "Ola mundo" na tela

print("Ola mundo")  # Exibe "Ola mundo" na tela

# criar_cachorro()  # Chama a função criar_cachorro


# OBSERVAÇÕES IMPORTANTES:

# OBSERVAÇÃO 1:
# Cachorro é uma CLASSE.
# A classe funciona como um molde para criar objetos/instâncias.

# OBSERVAÇÃO 2:
# __init__ é um MÉTODO ESPECIAL.
# Ele é executado automaticamente quando uma nova instância é criada.

# OBSERVAÇÃO 3:
# acordado=True possui um VALOR PADRÃO.
# Se nenhum valor for informado para acordado,
# o Python utilizará True.

# OBSERVAÇÃO 4:
# Nesta linha:
# c = Cachorro("Chappie", "amarelo")
#
# O valor de acordado não foi informado.
# Portanto, será utilizado o valor padrão:
# acordado = True

# OBSERVAÇÃO 5:
# Nesta linha:
# c = Cachorro("Zeus", "Branco e preto", False)
#
# O valor False foi informado para acordado.
# Portanto:
# nome = "Zeus"
# cor = "Branco e preto"
# acordado = False

# OBSERVAÇÃO 6:
# __del__ é outro MÉTODO ESPECIAL.
# Ele está relacionado à destruição da instância.

# OBSERVAÇÃO 7:
# del c remove a referência da variável c.
# Se não existirem outras referências para a instância,
# ela poderá ser destruída e __del__ poderá ser chamado.

# OBSERVAÇÃO 8:
# falar() é um MÉTODO da classe Cachorro.
# Ele representa um comportamento do objeto.

# OBSERVAÇÃO 9:
# criar_cachorro() é uma FUNÇÃO.
# Ela está fora da classe Cachorro.
# Portanto, não é um método da classe.

# OBSERVAÇÃO 10:
# A função criar_cachorro() não será executada
# porque a chamada está comentada:
#
# # criar_cachorro()

# OBSERVAÇÃO 11:
# c é uma INSTÂNCIA da classe Cachorro.
#
# Cachorro = CLASSE / MOLDE
# c = OBJETO / INSTÂNCIA

# OBSERVAÇÃO 12:
# self representa a própria instância.
#
# self.nome
# self.cor
# self.acordado
#
# São atributos pertencentes à instância.