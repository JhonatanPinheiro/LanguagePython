class Passaro:  # Define a classe Passaro

    def voar(self):  # Define o método voar
        print("Voando...")  # Mostra a mensagem "Voando..."


class Pardal(Passaro):  # Define Pardal herdando da classe Passaro

    def voar(self):  # Sobrescreve o método voar da classe Passaro
        print("Pardal pode voar")  # Mostra que o pardal pode voar


class Avestruz(Passaro):  # Define Avestruz herdando da classe Passaro

    def voar(self):  # Sobrescreve o método voar da classe Passaro
        print("Avestruz não pode voar")  # Mostra que o avestruz não pode voar


##NOTE: exemplo ruim do uso de herança para "ganhar" o método voar  # O avião não deveria herdar de Passaro
class Aviao(Passaro):  # Define Aviao herdando da classe Passaro
    def voar(self):  # Sobrescreve o método voar da classe Passaro
        print("Avião está decolando...")  # Mostra que o avião está decolando


def plano_voo(obj):  # Define uma função que recebe um objeto
    obj.voar()  # Chama o método voar do objeto recebido


plano_voo(Pardal())  # Cria um Pardal e chama seu método voar
plano_voo(Avestruz())  # Cria um Avestruz e chama seu método voar
plano_voo(Aviao())  # Cria um Avião e chama seu método voar