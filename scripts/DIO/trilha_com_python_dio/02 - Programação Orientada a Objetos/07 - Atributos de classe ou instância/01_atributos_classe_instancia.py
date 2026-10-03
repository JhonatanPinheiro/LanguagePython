class Estudante:  # Define a classe Estudante
    escola = "DIO"  # Define um atributo de classe compartilhado por todos os estudantes

    def __init__(self, nome, matricula):  # Inicializa o objeto recebendo nome e matrícula
        self.nome = nome  # Armazena o nome do estudante
        self.matricula = matricula  # Armazena a matrícula do estudante

    def __str__(self) -> str:  # Define como o objeto será representado como texto
        return f"{self.nome} - {self.matricula} - {self.escola}"  # Retorna nome, matrícula e escola


def mostrar_valores(*objs):  # Define uma função que pode receber vários objetos
    for obj in objs:  # Percorre cada objeto recebido
        print(obj)  # Mostra o objeto usando o método __str__


aluno_1 = Estudante("Jhonatan", 1)  # Cria o primeiro objeto Estudante
aluno_2 = Estudante("Giovanna", 2)  # Cria o segundo objeto Estudante
mostrar_valores(aluno_1, aluno_2)  # Mostra os dados dos dois estudantes

Estudante.escola = "Python"  # Altera o atributo de classe escola
aluno_3 = Estudante("Chappie", 3)  # Cria o terceiro objeto Estudante
mostrar_valores(aluno_1, aluno_2, aluno_3)  # Mostra os dados dos três estudantes