class Conta:  # Define a classe Conta

    def __init__(self, nro_agencia, saldo=0):  # Cria o objeto recebendo a agência e o saldo
        self._saldo = saldo  # Guarda o saldo dentro do objeto
        self.nro_agencia = nro_agencia  # Guarda o número da agência dentro do objeto

    def depositar(self, valor):  # Define o método para depositar um valor
        # ...  # Indica que aqui poderia existir alguma outra lógica
        self._saldo += valor  # Adiciona o valor ao saldo atual

    def sacar(self, valor):  # Define o método para sacar um valor
        # ...  # Indica que aqui poderia existir alguma outra lógica
        self._saldo -= valor  # Diminui o valor do saldo atual

    def mostrar_saldo(self):  # Define o método para consultar o saldo
        # ...  # Indica que aqui poderia existir alguma outra lógica
        return self._saldo  # Retorna o saldo atual


conta = Conta("0001", 500)  # Cria um objeto Conta com agência "0001" e saldo inicial 100
conta.depositar(4000)  # Adiciona 100 ao saldo da conta
conta.depositar(2000)


print(conta.nro_agencia)  # Mostra o número da agência
print(conta.mostrar_saldo())  # Mostra o saldo atual da conta







# ============================================================
# ENCAPSULAMENTO — POO
# ============================================================

# Encapsulamento é um conceito da Programação Orientada a Objetos
# que serve para proteger e controlar o acesso aos dados de um objeto.
#
# A ideia é evitar que qualquer parte do programa altere diretamente
# informações que deveriam ser controladas pela própria classe.


# ============================================================
# ATRIBUTO PÚBLICO
# ============================================================

# Um atributo público pode ser acessado diretamente de fora da classe.
#
# Em Python, normalmente utilizamos o nome do atributo sem nenhum
# caractere especial.
#
# Exemplo:
#
# self.nome
#
# Esse atributo pode ser acessado diretamente:
#
# pessoa.nome


# ============================================================
# ATRIBUTO PROTEGIDO
# ============================================================

# Um atributo com apenas UM underline (_) é considerado protegido
# por CONVENÇÃO.
#
# Exemplo:
#
# self._nome
#
# O underline significa:
# "Esse atributo é interno da classe e deve ser utilizado com cuidado."
#
# Porém, o Python ainda permite que ele seja acessado diretamente.
#
# Portanto, _nome NÃO é realmente privado.


# ============================================================
# ATRIBUTO PRIVADO
# ============================================================

# Um atributo com DOIS underlines (__) é tratado como privado.
#
# Exemplo:
#
# self.__saldo
#
# A intenção é impedir o acesso direto ao atributo fora da classe.
#
# Exemplo:
#
# conta.__saldo
#
# Não é a forma correta de acessar esse atributo.
#
# Normalmente, criamos métodos dentro da própria classe para
# controlar o acesso ou a alteração desse valor.


# ============================================================
# EXEMPLO DE ENCAPSULAMENTO
# ============================================================

# class Conta:
#
#     def __init__(self, saldo):
#         self.__saldo = saldo
#
#     def consultar_saldo(self):
#         return self.__saldo
#
#     def depositar(self, valor):
#         self.__saldo += valor


# Nesse exemplo:
#
# self.__saldo
#
# é um atributo privado.
#
# O saldo não é alterado diretamente de fora da classe.
#
# Utilizamos métodos para controlar o acesso:
#
# consultar_saldo()
# depositar()


# ============================================================
# RESUMO
# ============================================================

# self.nome
# -> Público
# -> Pode ser acessado diretamente de fora da classe.
#
#
# self._nome
# -> Protegido por convenção
# -> O Python permite acesso externo, mas indica que o atributo
#    deve ser tratado como interno.
#
#
# self.__nome
# -> Privado / name mangling
# -> O acesso direto é dificultado pelo Python.
#
#
# ENCAPSULAMENTO
# -> Protege os dados e controla como eles podem ser acessados
#    ou modificados.


# ============================================================
# PARA DECORAR
# ============================================================

# Público:
# "Pode acessar diretamente."
#
# Protegido:
# "É interno, mas o Python ainda permite acesso."
#
# Privado:
# "A classe controla o acesso."
#
# Encapsulamento:
# "Protege os dados e controla o acesso a eles."


# ============================================================
# OBSERVAÇÃO IMPORTANTE
# ============================================================

# Python não possui um "private" exatamente igual a algumas
# outras linguagens de programação.
#
# O __ é utilizado pelo Python para realizar um mecanismo chamado
# NAME MANGLING, que modifica internamente o nome do atributo.
#
# Por isso, para estudar:
#
# self.nome
# -> público
#
# self._nome
# -> protegido por convenção
#
# self.__nome
# -> privado / name mangling