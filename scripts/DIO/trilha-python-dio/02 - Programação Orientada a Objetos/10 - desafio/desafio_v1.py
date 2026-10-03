from abc import ABC, abstractclassmethod, abstractproperty  # Importa recursos para criar classes e métodos abstratos
from datetime import datetime  # Importa recursos para trabalhar com data e hora


class Cliente:  # Define a classe Cliente

    def __init__(self, endereco):  # Inicializa o cliente recebendo o endereço
        self.endereco = endereco  # Armazena o endereço do cliente
        self.contas = []  # Cria uma lista para armazenar as contas do cliente

    def realizar_transacao(self, conta, transacao):  # Define o método para realizar uma transação
        transacao.registrar(conta)  # Registra a transação na conta

    def adicionar_conta(self, conta):  # Define o método para adicionar uma conta ao cliente
        self.contas.append(conta)  # Adiciona a conta na lista de contas


class PessoaFisica(Cliente):  # Define PessoaFisica herdando de Cliente

    def __init__(self, nome, data_nascimento, cpf, endereco):  # Inicializa a pessoa física
        super().__init__(endereco)  # Chama o construtor da classe Cliente
        self.nome = nome  # Armazena o nome
        self.data_nascimento = data_nascimento  # Armazena a data de nascimento
        self.cpf = cpf  # Armazena o CPF


class Conta:  # Define a classe Conta

    def __init__(self, numero, cliente):  # Inicializa a conta recebendo número e cliente
        self._saldo = 0  # Define o saldo inicial como 0
        self._numero = numero  # Armazena o número da conta
        self._agencia = "0001"  # Define o número da agência
        self._cliente = cliente  # Armazena o cliente da conta
        self._historico = Historico()  # Cria um histórico para armazenar as transações

    @classmethod  # Define um método de classe
    def nova_conta(cls, cliente, numero):  # Cria uma nova conta
        return cls(numero, cliente)  # Retorna uma nova instância da classe

    @property  # Permite acessar saldo como uma propriedade
    def saldo(self):  # Define a propriedade saldo
        return self._saldo  # Retorna o saldo atual

    @property  # Permite acessar numero como uma propriedade
    def numero(self):  # Define a propriedade numero
        return self._numero  # Retorna o número da conta

    @property  # Permite acessar agencia como uma propriedade
    def agencia(self):  # Define a propriedade agencia
        return self._agencia  # Retorna o número da agência

    @property  # Permite acessar cliente como uma propriedade
    def cliente(self):  # Define a propriedade cliente
        return self._cliente  # Retorna o cliente da conta

    @property  # Permite acessar historico como uma propriedade
    def historico(self):  # Define a propriedade historico
        return self._historico  # Retorna o histórico da conta

    def sacar(self, valor):  # Define o método para realizar um saque
        saldo = self.saldo  # Obtém o saldo atual
        excedeu_saldo = valor > saldo  # Verifica se o saque é maior que o saldo

        if excedeu_saldo:  # Verifica se não há saldo suficiente
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")  # Mostra uma mensagem de erro

        elif valor > 0:  # Verifica se o valor do saque é maior que zero
            self._saldo -= valor  # Diminui o valor do saque do saldo
            print("\n=== Saque realizado com sucesso! ===")  # Mostra uma mensagem de sucesso
            return True  # Informa que o saque foi realizado

        else:  # Executa quando o valor é inválido
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mostra uma mensagem de erro

        return False  # Informa que o saque não foi realizado

    def depositar(self, valor):  # Define o método para realizar um depósito
        if valor > 0:  # Verifica se o valor é maior que zero
            self._saldo += valor  # Adiciona o valor ao saldo
            print("\n=== Depósito realizado com sucesso! ===")  # Mostra uma mensagem de sucesso
        else:  # Executa quando o valor é inválido
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mostra uma mensagem de erro
            return False  # Informa que o depósito não foi realizado

        return True  # Informa que o depósito foi realizado


class ContaCorrente(Conta):  # Define ContaCorrente herdando de Conta

    def __init__(self, numero, cliente, limite=500, limite_saques=3):  # Inicializa a conta corrente
        super().__init__(numero, cliente)  # Chama o construtor da classe Conta
        self.limite = limite  # Define o limite máximo para saque
        self.limite_saques = limite_saques  # Define a quantidade máxima de saques

    def sacar(self, valor):  # Sobrescreve o método sacar da classe Conta
        numero_saques = len(  # Conta quantos saques já foram realizados
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]  # Filtra somente as transações de saque
        )

        excedeu_limite = valor > self.limite  # Verifica se o saque ultrapassa o limite
        excedeu_saques = numero_saques >= self.limite_saques  # Verifica se atingiu o limite de saques

        if excedeu_limite:  # Verifica se o valor ultrapassa o limite
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")  # Mostra uma mensagem de erro

        elif excedeu_saques:  # Verifica se atingiu o limite de saques
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")  # Mostra uma mensagem de erro

        else:  # Executa quando os limites não foram ultrapassados
            return super().sacar(valor)  # Chama o método sacar da classe Conta

        return False  # Informa que o saque não foi realizado

    def __str__(self):  # Define como a conta será representada como texto
        return f"""\  # Retorna os dados da conta formatados
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:  # Define a classe Historico

    def __init__(self):  # Inicializa o histórico
        self._transacoes = []  # Cria uma lista para armazenar as transações

    @property  # Permite acessar transacoes como uma propriedade
    def transacoes(self):  # Define a propriedade transacoes
        return self._transacoes  # Retorna a lista de transações

    def adicionar_transacao(self, transacao):  # Adiciona uma transação ao histórico
        self._transacoes.append(  # Adiciona uma nova transação na lista
            {
                "tipo": transacao.__class__.__name__,  # Armazena o nome da classe da transação
                "valor": transacao.valor,  # Armazena o valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Armazena a data e hora da transação
            }
        )


class Transacao(ABC):  # Define uma classe abstrata para as transações

    @property  # Define valor como uma propriedade
    @abstractproperty  # Torna a propriedade obrigatória nas classes filhas
    def valor(self):  # Define a propriedade valor
        pass  # Não possui implementação na classe abstrata

    @abstractclassmethod  # Define registrar como um método abstrato
    def registrar(self, conta):  # Define o método para registrar uma transação
        pass  # Não possui implementação na classe abstrata


class Saque(Transacao):  # Define Saque herdando de Transacao

    def __init__(self, valor):  # Inicializa o saque recebendo um valor
        self._valor = valor  # Armazena o valor do saque

    @property  # Permite acessar valor como uma propriedade
    def valor(self):  # Define a propriedade valor
        return self._valor  # Retorna o valor do saque

    def registrar(self, conta):  # Registra o saque na conta
        sucesso_transacao = conta.sacar(self.valor)  # Tenta realizar o saque

        if sucesso_transacao:  # Verifica se o saque foi realizado com sucesso
            conta.historico.adicionar_transacao(self)  # Adiciona o saque ao histórico


class Deposito(Transacao):  # Define Deposito herdando de Transacao

    def __init__(self, valor):  # Inicializa o depósito recebendo um valor
        self._valor = valor  # Armazena o valor do depósito

    @property  # Permite acessar valor como uma propriedade
    def valor(self):  # Define a propriedade valor
        return self._valor  # Retorna o valor do depósito

    def registrar(self, conta):  # Registra o depósito na conta
        sucesso_transacao = conta.depositar(self.valor)  # Tenta realizar o depósito

        if sucesso_transacao:  # Verifica se o depósito foi realizado com sucesso
            conta.historico.adicionar_transacao(self)  # Adiciona o depósito ao histórico