class Veiculo:  # Define uma classe chamada Veiculo

    def __init__(self, cor, placa, numero_rodas):  # Método construtor da classe Veiculo
        self.cor = cor  # Cria o atributo cor
        self.placa = placa  # Cria o atributo placa
        self.numero_rodas = numero_rodas  # Cria o atributo numero_rodas

    def ligar_motor(self):  # Define o método ligar_motor
        print("Ligando o motor")  # Exibe uma mensagem informando que o motor está sendo ligado

    def __str__(self):  # Método especial utilizado quando o objeto é convertido para texto
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  # Retorna o nome da classe e seus atributos


class Motocicleta(Veiculo):  # Define a classe Motocicleta herdando da classe Veiculo
    pass  # Indica que a classe não possui implementação própria neste momento


class Carro(Veiculo):  # Define a classe Carro herdando da classe Veiculo
    pass  # Indica que a classe não possui implementação própria neste momento


class Caminhao(Veiculo):  # Define a classe Caminhao herdando da classe Veiculo

    def __init__(self, cor, placa, numero_rodas, carregado):  # Define o construtor próprio da classe Caminhao
        super().__init__(cor, placa, numero_rodas)  # Chama o construtor da classe Veiculo
        self.carregado = carregado  # Cria o atributo carregado específico do Caminhao

    def esta_carregado(self):  # Define o método esta_carregado
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")  # Verifica se carregado é True ou False e exibe a mensagem correspondente


moto = Motocicleta("preta", "abc-1234", 2)  # Cria um objeto da classe Motocicleta
carro = Carro("branco", "xde-0098", 4)  # Cria um objeto da classe Carro
caminhao = Caminhao("roxo", "gfd-8712", 8, True)  # Cria um objeto da classe Caminhao

print(moto)  # Exibe o objeto moto utilizando o método __str__
print(carro)  # Exibe o objeto carro utilizando o método __str__
print(caminhao)  # Exibe o objeto caminhao utilizando o método __str__


# OBSERVAÇÕES IMPORTANTES:

# OBSERVAÇÃO 1:
# Veiculo é a CLASSE PAI.
# Motocicleta, Carro e Caminhao são CLASSES FILHAS.

# OBSERVAÇÃO 2:
# Motocicleta(Veiculo)
# significa que Motocicleta HERDA da classe Veiculo.

# OBSERVAÇÃO 3:
# Carro(Veiculo)
# significa que Carro HERDA da classe Veiculo.

# OBSERVAÇÃO 4:
# Caminhao(Veiculo)
# significa que Caminhao HERDA da classe Veiculo.

# OBSERVAÇÃO 5:
# As classes Motocicleta e Carro utilizam pass.
# Isso significa que elas não possuem uma implementação própria.
# Elas herdam os comportamentos da classe Veiculo.

# OBSERVAÇÃO 6:
# Por causa da HERANÇA, Motocicleta e Carro
# possuem acesso aos métodos de Veiculo.
#
# Por exemplo:
# moto.ligar_motor()
# carro.ligar_motor()

# OBSERVAÇÃO 7:
# super() permite acessar a classe PAI.
#
# super().__init__(cor, placa, numero_rodas)
#
# Nesse caso, o Caminhao utiliza o __init__ da classe Veiculo
# para inicializar cor, placa e numero_rodas.

# OBSERVAÇÃO 8:
# O Caminhao possui um atributo adicional:
#
# self.carregado = carregado
#
# Esse atributo não existe no Veiculo.

# OBSERVAÇÃO 9:
# Caminhao possui um método próprio:
#
# esta_carregado()
#
# Esse método não existe na classe Veiculo.

# OBSERVAÇÃO 10:
# O valor True foi passado para carregado:
#
# caminhao = Caminhao("roxo", "gfd-8712", 8, True)
#
# Portanto:
# self.carregado = True

# OBSERVAÇÃO 11:
# __str__ é um MÉTODO ESPECIAL.
# Ele define como o objeto será apresentado quando usamos print().
#
# Por exemplo:
# print(moto)
#
# chama automaticamente:
# moto.__str__()

# OBSERVAÇÃO 12:
# self.__dict__ contém os atributos do objeto.
#
# No objeto caminhao, teremos:
# cor
# placa
# numero_rodas
# carregado

# OBSERVAÇÃO 13:
# __class__.__name__ obtém o nome da classe do objeto.
#
# Para moto:
# Motocicleta
#
# Para carro:
# Carro
#
# Para caminhao:
# Caminhao