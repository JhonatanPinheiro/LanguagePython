from datetime import datetime  # Importa datetime para trabalhar com data e hora

class Pessoa:  # Define a classe Pessoa

    def __init__(self, nome, ano_nascimento):  # Inicializa o objeto recebendo nome e ano de nascimento
        self.nome = nome  # Armazena o nome da pessoa
        self._ano_nascimento = ano_nascimento  # Armazena o ano de nascimento

    @property  # Permite acessar idade como se fosse um atributo
    def idade(self):  # Define o método que calcula a idade

        # _ano_atual = 2022  # Define o ano atual manualmente

        _ano_atual = datetime.now().year  # Pega automaticamente o ano atual do computador

        return _ano_atual - self._ano_nascimento  # Calcula e retorna a idade


pessoa = Pessoa("Jhonatan", 1999)  # Cria um objeto Pessoa com nome e ano de nascimento

print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")  # Mostra o nome e a idade da pessoa