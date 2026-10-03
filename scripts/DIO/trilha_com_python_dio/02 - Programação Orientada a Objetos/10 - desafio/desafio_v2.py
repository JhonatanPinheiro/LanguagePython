import textwrap  # Importa recursos para trabalhar com textos formatados

from abc import ABC, abstractclassmethod, abstractproperty  # Importa recursos para classes e métodos abstratos

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
        self._historico = Historico()  # Cria o histórico da conta

    @classmethod  # Define um método de classe
    def nova_conta(cls, cliente, numero):  # Define um método para criar uma nova conta
        return cls(numero, cliente)  # Cria e retorna uma nova conta

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
        saldo = self.saldo  # Obtém o saldo atual da conta
        excedeu_saldo = valor > saldo  # Verifica se o valor é maior que o saldo

        if excedeu_saldo:  # Verifica se não existe saldo suficiente
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")  # Mostra mensagem de erro

        elif valor > 0:  # Verifica se o valor do saque é maior que zero
            self._saldo -= valor  # Diminui o valor do saque do saldo
            print("\n=== Saque realizado com sucesso! ===")  # Mostra mensagem de sucesso
            return True  # Retorna True indicando que o saque foi realizado

        else:  # Executa quando o valor informado é inválido
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mostra mensagem de erro

        return False  # Retorna False indicando que o saque não foi realizado

    def depositar(self, valor):  # Define o método para realizar um depósito
        if valor > 0:  # Verifica se o valor é maior que zero
            self._saldo += valor  # Adiciona o valor ao saldo
            print("\n=== Depósito realizado com sucesso! ===")  # Mostra mensagem de sucesso

        else:  # Executa quando o valor informado é inválido
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")  # Mostra mensagem de erro
            return False  # Retorna False indicando que o depósito não foi realizado

        return True  # Retorna True indicando que o depósito foi realizado


class ContaCorrente(Conta):  # Define ContaCorrente herdando de Conta

    def __init__(self, numero, cliente, limite=500, limite_saques=3):  # Inicializa a conta corrente
        super().__init__(numero, cliente)  # Chama o construtor da classe Conta
        self._limite = limite  # Armazena o limite de saque
        self._limite_saques = limite_saques  # Armazena o limite de quantidade de saques

    def sacar(self, valor):  # Sobrescreve o método sacar da classe Conta

        numero_saques = len(  # Conta a quantidade de saques realizados
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]  # Filtra somente as transações de saque
        )

        excedeu_limite = valor > self._limite  # Verifica se o valor ultrapassa o limite de saque
        excedeu_saques = numero_saques >= self._limite_saques  # Verifica se atingiu o limite de saques

        if excedeu_limite:  # Verifica se o valor ultrapassou o limite
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")  # Mostra mensagem de erro

        elif excedeu_saques:  # Verifica se o número máximo de saques foi atingido
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")  # Mostra mensagem de erro

        else:  # Executa quando nenhuma das regras anteriores foi violada
            return super().sacar(valor)  # Chama o método sacar da classe Conta

        return False  # Retorna False indicando que o saque não foi realizado

    def __str__(self):  # Define como o objeto ContaCorrente será exibido como texto
        return f"""\  # Retorna os dados da conta formatados
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:  # Define a classe responsável pelo histórico

    def __init__(self):  # Inicializa o histórico
        self._transacoes = []  # Cria uma lista para armazenar as transações

    @property  # Permite acessar transacoes como uma propriedade
    def transacoes(self):  # Define a propriedade transacoes
        return self._transacoes  # Retorna a lista de transações

    def adicionar_transacao(self, transacao):  # Define o método para adicionar uma transação
        self._transacoes.append(  # Adiciona uma nova transação à lista
            {
                "tipo": transacao.__class__.__name__,  # Armazena o nome da classe da transação
                "valor": transacao.valor,  # Armazena o valor da transação
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),  # Armazena a data e hora
            }
        )


class Transacao(ABC):  # Define uma classe abstrata para as transações

    @property  # Define valor como uma propriedade
    @abstractproperty  # Torna a propriedade obrigatória nas classes filhas
    def valor(self):  # Define a propriedade valor
        pass  # Não possui implementação aqui

    @abstractclassmethod  # Define um método abstrato obrigatório nas classes filhas
    def registrar(self, conta):  # Define o método para registrar uma transação
        pass  # Não possui implementação aqui


class Saque(Transacao):  # Define Saque herdando de Transacao

    def __init__(self, valor):  # Inicializa o saque recebendo o valor
        self._valor = valor  # Armazena o valor do saque

    @property  # Permite acessar valor como uma propriedade
    def valor(self):  # Define a propriedade valor
        return self._valor  # Retorna o valor do saque

    def registrar(self, conta):  # Define o método para registrar o saque
        sucesso_transacao = conta.sacar(self.valor)  # Tenta realizar o saque na conta

        if sucesso_transacao:  # Verifica se o saque foi realizado com sucesso
            conta.historico.adicionar_transacao(self)  # Adiciona o saque ao histórico


class Deposito(Transacao):  # Define Deposito herdando de Transacao

    def __init__(self, valor):  # Inicializa o depósito recebendo o valor
        self._valor = valor  # Armazena o valor do depósito

    @property  # Permite acessar valor como uma propriedade
    def valor(self):  # Define a propriedade valor
        return self._valor  # Retorna o valor do depósito

    def registrar(self, conta):  # Define o método para registrar o depósito
        sucesso_transacao = conta.depositar(self.valor)  # Tenta realizar o depósito na conta

        if sucesso_transacao:  # Verifica se o depósito foi realizado com sucesso
            conta.historico.adicionar_transacao(self)  # Adiciona o depósito ao histórico


def menu():  # Define a função responsável por exibir o menu

    menu = """\n  # Cria uma string contendo as opções do menu

    ================ MENU ================  # Exibe o título do menu

    [d]\tDepositar  # Opção para realizar depósito
    [s]\tSacar  # Opção para realizar saque
    [e]\tExtrato  # Opção para consultar o extrato
    [nc]\tNova conta  # Opção para criar uma nova conta
    [lc]\tListar contas  # Opção para listar as contas
    [nu]\tNovo usuário  # Opção para criar um novo usuário
    [q]\tSair  # Opção para sair do sistema

    => """  # Solicita ao usuário que escolha uma opção

    return input(textwrap.dedent(menu))  # Mostra o menu e recebe a opção escolhida


def filtrar_cliente(cpf, clientes):  # Define a função para localizar um cliente pelo CPF

    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]  # Filtra os clientes pelo CPF

    return clientes_filtrados[0] if clientes_filtrados else None  # Retorna o cliente ou None se não encontrar


def recuperar_conta_cliente(cliente):  # Define a função para recuperar a conta do cliente

    if not cliente.contas:  # Verifica se o cliente não possui contas
        print("\n@@@ Cliente não possui conta! @@@")  # Mostra mensagem informando que não há conta
        return  # Encerra a função

    # FIXME: não permite cliente escolher a conta  # Indica que atualmente o cliente não pode escolher a conta

    return cliente.contas[0]  # Retorna a primeira conta do cliente


def depositar(clientes):  # Define a função para realizar um depósito

    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Procura o cliente pelo CPF

    if not cliente:  # Verifica se o cliente não foi encontrado
        print("\n@@@ Cliente não encontrado! @@@")  # Mostra mensagem de erro
        return  # Encerra a função

    valor = float(input("Informe o valor do depósito: "))  # Solicita o valor do depósito
    transacao = Deposito(valor)  # Cria uma transação de depósito
    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente

    if not conta:  # Verifica se o cliente não possui conta
        return  # Encerra a função

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação na conta


def sacar(clientes):  # Define a função para realizar um saque

    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Procura o cliente pelo CPF

    if not cliente:  # Verifica se o cliente não foi encontrado
        print("\n@@@ Cliente não encontrado! @@@")  # Mostra mensagem de erro
        return  # Encerra a função

    valor = float(input("Informe o valor do saque: "))  # Solicita o valor do saque
    transacao = Saque(valor)  # Cria uma transação de saque
    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente

    if not conta:  # Verifica se o cliente não possui conta
        return  # Encerra a função

    cliente.realizar_transacao(conta, transacao)  # Realiza a transação na conta


def exibir_extrato(clientes):  # Define a função para exibir o extrato

    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Procura o cliente pelo CPF

    if not cliente:  # Verifica se o cliente não foi encontrado
        print("\n@@@ Cliente não encontrado! @@@")  # Mostra mensagem de erro
        return  # Encerra a função

    conta = recuperar_conta_cliente(cliente)  # Recupera a conta do cliente

    if not conta:  # Verifica se o cliente não possui conta
        return  # Encerra a função

    print("\n================ EXTRATO ================")  # Exibe o título do extrato

    transacoes = conta.historico.transacoes  # Recupera as transações do histórico
    extrato = ""  # Cria uma string vazia para armazenar o extrato

    if not transacoes:  # Verifica se não existem transações
        extrato = "Não foram realizadas movimentações."  # Define a mensagem para nenhuma movimentação

    else:  # Executa quando existem transações

        for transacao in transacoes:  # Percorre cada transação
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"  # Adiciona a transação ao extrato

    print(extrato)  # Mostra o extrato

    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")  # Mostra o saldo atual da conta

    print("==========================================")  # Exibe a linha final do extrato


def criar_cliente(clientes):  # Define a função para criar um novo cliente

    cpf = input("Informe o CPF (somente número): ")  # Solicita o CPF
    cliente = filtrar_cliente(cpf, clientes)  # Verifica se o CPF já está cadastrado

    if cliente:  # Verifica se já existe um cliente com esse CPF
        print("\n@@@ Já existe cliente com esse CPF! @@@")  # Mostra mensagem de erro
        return  # Encerra a função

    nome = input("Informe o nome completo: ")  # Solicita o nome
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")  # Solicita a data de nascimento
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")  # Solicita o endereço

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)  # Cria um novo cliente

    clientes.append(cliente)  # Adiciona o cliente à lista de clientes

    print("\n=== Cliente criado com sucesso! ===")  # Mostra mensagem de sucesso


def criar_conta(numero_conta, clientes, contas):  # Define a função para criar uma nova conta

    cpf = input("Informe o CPF do cliente: ")  # Solicita o CPF do cliente
    cliente = filtrar_cliente(cpf, clientes)  # Procura o cliente pelo CPF

    if not cliente:  # Verifica se o cliente não foi encontrado
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")  # Mostra mensagem de erro
        return  # Encerra a função

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)  # Cria uma nova conta corrente

    contas.append(conta)  # Adiciona a conta à lista de contas

    cliente.contas.append(conta)  # Adiciona a conta à lista de contas do cliente

    print("\n=== Conta criada com sucesso! ===")  # Mostra mensagem de sucesso


def listar_contas(contas):  # Define a função para listar as contas

    for conta in contas:  # Percorre todas as contas
        print("=" * 100)  # Exibe uma linha de separação
        print(textwrap.dedent(str(conta)))  # Mostra os dados da conta formatados


def main():  # Define a função principal do programa

    clientes = []  # Cria uma lista para armazenar os clientes
    contas = []  # Cria uma lista para armazenar as contas

    while True:  # Mantém o sistema funcionando até o usuário escolher sair

        opcao = menu()  # Exibe o menu e recebe a opção escolhida

        if opcao == "d":  # Verifica se a opção escolhida foi depósito
            depositar(clientes)  # Chama a função de depósito

        elif opcao == "s":  # Verifica se a opção escolhida foi saque
            sacar(clientes)  # Chama a função de saque

        elif opcao == "e":  # Verifica se a opção escolhida foi extrato
            exibir_extrato(clientes)  # Chama a função de exibir extrato

        elif opcao == "nu":  # Verifica se a opção escolhida foi novo usuário
            criar_cliente(clientes)  # Chama a função para criar cliente

        elif opcao == "nc":  # Verifica se a opção escolhida foi nova conta
            numero_conta = len(contas) + 1  # Gera o número da nova conta
            criar_conta(numero_conta, clientes, contas)  # Chama a função para criar a conta

        elif opcao == "lc":  # Verifica se a opção escolhida foi listar contas
            listar_contas(contas)  # Chama a função para listar as contas

        elif opcao == "q":  # Verifica se a opção escolhida foi sair
            break  # Encerra o loop e termina o programa

        else:  # Executa quando a opção informada não existe
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")  # Mostra mensagem de erro


main()  # Executa a função principal do programa