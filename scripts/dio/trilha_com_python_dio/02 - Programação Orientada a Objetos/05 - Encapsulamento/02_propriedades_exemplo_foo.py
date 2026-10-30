class Foo:  # Define a classe Foo

    def __init__(self, x=None):  # Inicializa o objeto recebendo x, que por padrão é None
        self._x = x  # Armazena o valor de x no atributo _x

    @property  # Permite acessar x como se fosse um atributo
    def x(self):  # Define o método para consultar o valor de x
        return self._x or 0  # Retorna _x; se _x for None ou outro valor considerado falso, retorna 0

    @x.setter  # Define o que acontece quando atribuímos um valor para x
    def x(self, value):  # Recebe o valor que será atribuído a x
        self._x += value  # Adiciona o valor recebido ao valor atual de _x

    @x.deleter  # Define o que acontece quando usamos del foo.x
    def x(self):  # Define o método executado ao deletar x
        self._x = 0  # Define _x como 0


foo = Foo(10)  # Cria um objeto Foo com _x começando em 10
print(foo.x)  # Acessa x através da propriedade e mostra 10

del foo.x  # Executa o deleter e define _x como 0
print(foo.x)  # Acessa x e mostra 0

foo.x = 10  # Executa o setter e adiciona 10 ao _x
print(foo.x)  # Acessa x e mostra 10






# ============================================================
# @property — EXPLICAÇÃO
# ============================================================

# O @property permite usar um MÉTODO como se fosse um ATRIBUTO.
#
# Ou seja, normalmente uma função seria chamada assim:
#
# objeto.valor()
#
# Mas com @property podemos fazer:
#
# objeto.valor
#
# O Python executa a função por trás do @property
# automaticamente.


# ============================================================
# 🧠 IDEIA PRINCIPAL
# ============================================================

# Pense no @property como uma PORTA.
#
# O atributo fica protegido dentro do objeto:
#
# self._valor
#
# E o @property cria uma porta para controlar o acesso:
#
# objeto.valor
#
# Então:
#
# objeto.valor
#       ↓
#     @property
#       ↓
# acessa self._valor


# ============================================================
# @property — CONTROLA A LEITURA
# ============================================================

# Exemplo:
#
# class Pessoa:
#
#     def __init__(self, nome):
#         self._nome = nome
#
#     @property
#     def nome(self):
#         return self._nome
#
#
# pessoa = Pessoa("Jhonatan")
#
# print(pessoa.nome)
#
# Perceba que usamos:
#
# pessoa.nome
#
# e NÃO:
#
# pessoa.nome()
#
# O @property faz o método parecer um atributo.


# ============================================================
# @setter — CONTROLA A ALTERAÇÃO
# ============================================================

# O setter é utilizado quando queremos controlar
# o que acontece quando alguém tenta ALTERAR um atributo.
#
# Exemplo real: uma conta bancária.
#
# class Conta:
#
#     def __init__(self, saldo):
#         self._saldo = saldo
#
#     @property
#     def saldo(self):
#         return self._saldo
#
#     @saldo.setter
#     def saldo(self, valor):
#         if valor < 0:
#             print("Saldo não pode ser negativo!")
#         else:
#             self._saldo = valor
#
#
# conta = Conta(1000)
#
# print(conta.saldo)
#
# Resultado:
#
# 1000
#
#
# Agora:
#
# conta.saldo = -500
#
# O setter é chamado automaticamente.
#
# Ele verifica:
#
# if valor < 0:
#
# Como -500 é menor que 0, o valor é rejeitado.


# ============================================================
# 🏦 EXEMPLO REAL — CONTA BANCÁRIA
# ============================================================

# Imagine que temos:
#
# conta.saldo = -500
#
# Sem uma regra, poderíamos acabar permitindo um
# valor inválido.
#
# Com @property + setter:
#
# conta.saldo = -500
#        ↓
#     @setter
#        ↓
# verifica o valor
#        ↓
# -500 é inválido
#        ↓
#       ❌
#
# O setter funciona como um "segurança" que verifica
# se o valor pode ou não entrar.


# ============================================================
# 🌡️ EXEMPLO REAL — TEMPERATURA
# ============================================================

# Imagine uma máquina que possui uma temperatura.
#
# class Maquina:
#
#     def __init__(self, temperatura):
#         self._temperatura = temperatura
#
#     @property
#     def temperatura(self):
#         return self._temperatura
#
#     @temperatura.setter
#     def temperatura(self, valor):
#         if valor < 0:
#             raise ValueError("Temperatura não pode ser menor que 0!")
#
#         self._temperatura = valor
#
#
# maquina = Maquina(30)
#
# print(maquina.temperatura)
#
# Resultado:
#
# 30
#
#
# Agora alguém tenta:
#
# maquina.temperatura = -50
#
# O setter entra em ação:
#
# maquina.temperatura = -50
#          ↓
#       @setter
#          ↓
# verifica o valor
#          ↓
# -50 é inválido
#          ↓
#        ❌ ERRO


# ============================================================
# 🧠 QUANDO USAR @property?
# ============================================================

# Use @property quando você quer que algo PAREÇA um atributo,
# mas quer colocar uma REGRA por trás dele.
#
# Exemplo:
#
# objeto.valor
#
# Parece apenas um atributo.
#
# Mas por trás pode existir:
#
# - validação
# - cálculo
# - proteção
# - transformação de dados
# - regras de negócio
#
# Ou seja:
#
# "Eu quero acessar como um atributo,
# mas quero controlar o que acontece."


# ============================================================
# 🎯 PARA DECORAR
# ============================================================

# @property
# -> Controla a LEITURA.
#
# Quando fazemos:
#
# objeto.valor
#
# o @property é executado.


# @setter
# -> Controla a ALTERAÇÃO.
#
# Quando fazemos:
#
# objeto.valor = alguma_coisa
#
# o setter é executado.


# @deleter
# -> Controla a EXCLUSÃO.
#
# Quando fazemos:
#
# del objeto.valor
#
# o deleter é executado.


# ============================================================
# 🚪 ANALOGIA DA PORTA
# ============================================================

# Imagine que self._valor está dentro de uma sala.
#
# self._valor
#     ↓
# ┌───────────────┐
# │     SALA      │
# │               │
# │   _valor      │
# │               │
# └───────┬───────┘
#         │
#         🚪
#      @property
#
# O @property é a PORTA que controla como podemos
# acessar aquilo que está dentro da sala.


# Para LER:
#
# objeto.valor
#      ↓
# @property


# Para ALTERAR:
#
# objeto.valor = 10
#      ↓
# @setter


# Para EXCLUIR:
#
# del objeto.valor
#      ↓
# @deleter


# ============================================================
# ⭐ RESUMO FINAL
# ============================================================

# @property = controla a LEITURA
#
# @setter = controla a ALTERAÇÃO
#
# @deleter = controla a EXCLUSÃO
#
# E a principal ideia é:
#
# "Quero usar como um atributo,
# mas quero controlar o que acontece por trás."
#
# Essa é a grande finalidade do @property em Python.