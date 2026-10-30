class Pessoa:  # Define a classe Pessoa

    def __init__(self, nome, idade):  # Inicializa o objeto recebendo nome e idade
        self.nome = nome  # Armazena o nome da pessoa
        self.idade = idade  # Armazena a idade da pessoa

    @classmethod  # Define um método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):  # Cria uma Pessoa usando a data de nascimento
        idade = 2022 - ano  # Calcula a idade com base no ano de nascimento
        return cls(nome, idade)  # Cria e retorna um novo objeto Pessoa

    @staticmethod  # Define um método estático
    def e_maior_idade(idade):  # Recebe uma idade para verificar se é maior de idade
        return idade >= 18  # Retorna True se a idade for 18 ou mais


p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")  # Cria uma Pessoa usando o método de classe
print(p.nome, p.idade)  # Mostra o nome e a idade da pessoa

print(Pessoa.e_maior_idade(18))  # Verifica se 18 anos é maior de idade
print(Pessoa.e_maior_idade(8))  # Verifica se 8 anos é maior de idade



'''
# ============================================================
# EXEMPLO DE @classmethod E @staticmethod
# ============================================================


# Criamos a classe Produto.
# Podemos imaginar que ela é uma "fábrica" de produtos.
class Produto:

    # O __init__ é executado quando criamos um objeto Produto.
    # Ele recebe o nome e o preço do produto.
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    # ========================================================
    # @classmethod
    # ========================================================

    # O @classmethod cria um método que pertence à classe.
    # Em vez de receber "self", ele recebe "cls".
    #
    # self = um objeto específico
    # cls  = a própria classe Produto
    #
    # Neste exemplo, vamos usar o @classmethod para criar
    # um Produto de uma maneira diferente.
    @classmethod
    def criar_do_banco(cls, dados):

        # Imagine que o banco de dados entregou os dados
        # desta forma:
        #
        # "Notebook;3000"
        #
        # O split(";") separa as informações.
        nome, preco = dados.split(";")

        # Transformamos o preço de texto para número.
        preco = float(preco)

        # cls representa a classe Produto.
        #
        # Então:
        #
        # return cls(nome, preco)
        #
        # é praticamente a mesma coisa que:
        #
        # return Produto(nome, preco)
        #
        # Ou seja:
        # "Classe Produto, crie um novo objeto para mim."
        return cls(nome, preco)


    # ========================================================
    # @staticmethod
    # ========================================================

    # O @staticmethod cria um método que NÃO precisa
    # de self e também NÃO precisa de cls.
    #
    # Ele simplesmente realiza uma tarefa relacionada
    # à classe.
    #
    # Neste exemplo, vamos verificar se o preço é válido.
    @staticmethod
    def preco_valido(preco):

        # Verifica se o preço é maior que zero.
        #
        # Se for:
        #     True
        #
        # Se não for:
        #     False
        return preco > 0


# ============================================================
# USANDO O @classmethod
# ============================================================

# O banco de dados nos entregou:
#
# "Notebook;3000"
#
# O @classmethod vai separar esses dados e criar
# um objeto Produto.
produto = Produto.criar_do_banco("Notebook;3000")


# Agora temos um objeto chamado produto.
# Podemos acessar seus atributos usando o objeto.
print(produto.nome)
print(produto.preco)


# ============================================================
# USANDO O @staticmethod
# ============================================================

# Chamamos o método diretamente pela classe.
#
# Não precisamos criar outro objeto para fazer essa verificação.
#
# Estamos perguntando:
#
# "O preço 3000 é maior que zero?"
print(Produto.preco_valido(3000))


# Estamos perguntando:
#
# "O preço -10 é maior que zero?"
print(Produto.preco_valido(-10))


# ============================================================
# RESULTADO
# ============================================================

# O programa mostrará:
#
# Notebook
# 3000.0
# True
# False


# ============================================================
# RESUMINDO
# ============================================================

# @classmethod
# -> Recebe "cls".
# -> "cls" representa a própria classe.
# -> Pode ser usado para criar objetos de maneiras diferentes.
#
# Exemplo:
# Produto.criar_do_banco("Notebook;3000")


# @staticmethod
# -> Não recebe "self".
# -> Não recebe "cls".
# -> É usado para executar uma tarefa relacionada à classe,
#    mas que não precisa conhecer nenhum objeto ou a própria
#    classe.
#
# Exemplo:
# Produto.preco_valido(3000)

'''
