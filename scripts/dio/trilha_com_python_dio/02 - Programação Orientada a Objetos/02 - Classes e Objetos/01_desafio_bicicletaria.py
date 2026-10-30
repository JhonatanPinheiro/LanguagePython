class Bicicleta:  # Define uma classe chamada Bicicleta

    def __init__(self, cor, modelo, ano, valor,tipo,quantidade_de_marcha):  # Método construtor da classe, executado ao criar um objeto
        self.cor = cor  # Define o atributo cor do objeto
        self.modelo = modelo  # Define o atributo modelo do objeto
        self.ano = ano  # Define o atributo ano do objeto
        self.valor = valor  # Define o atributo valor do objeto
        self.tipo = tipo # Define o atributo valor do objeto
        self.quantidade_de_marcha = quantidade_de_marcha # Define o atributo valor do objeto
        
    def buzinar(self):  # Define o método buzinar
        print("Plim plim...")  # Exibe o som da buzina

    def parar(self):  # Define o método parar
        print("Parando bicicleta...")  # Exibe a mensagem de que a bicicleta está parando
        print("Bicicleta parada!")  # Exibe a mensagem de que a bicicleta parou

    def correr(self):  # Define o método correr
        print("Vrummmmm...")  # Exibe o som da bicicleta em movimento
    
    def revisao(self):
        print('Manutenção/Revisão Realizada!')
    
    def trocar_marcha(self, numero_da_troca):  # Define o método para trocar a marcha
         match numero_da_troca:  # Verifica o valor informado para a marcha
             
            case "R":  # Caso escolha R, representa a marcha Ré
                print(f"Marcha trocada para: ({numero_da_troca}) - Marcha Ré")
            
            case 1:  # Caso a marcha seja 1
                print(f"Marcha trocada para: ({numero_da_troca}) - Primeira Marcha")

            case 2:  # Caso a marcha seja 2
                print(f"Marcha trocada para: ({numero_da_troca}) - Segunda Marcha")

            case 3:  # Caso a marcha seja 3
                print(f"Marcha trocada para: ({numero_da_troca}) - Terceira Marcha")

            case 4:  # Caso a marcha seja 4
                print(f"Marcha trocada para: ({numero_da_troca}) - Quarta Marcha")

            case 5:  # Caso a marcha seja 5
                print(f"Troca de Marcha para: ({numero_da_troca}) - Quinta Marcha")

            case 6:  # Caso a marcha seja 6
                print(f"Troca de Marcha para: ({numero_da_troca}) - Sexta Marcha")

            case 7:  # Caso a marcha seja 7
                print(f"Marcha trocada para: ({numero_da_troca}) - Sétima Marcha")

            case 8:  # Caso a marcha seja 8
                print(f"Marcha trocada para: ({numero_da_troca}) - Oitava Marcha")

            case 9:  # Caso a marcha seja 9
                print(f"Marcha trocada para: ({numero_da_troca}) - Nona Marcha")

            case 10:  # Caso a marcha seja 10
                print(f"Marcha trocada para: ({numero_da_troca}) - Décima Marcha")

            case 11:  # Caso a marcha seja 11
                print(f"Marcha trocada para: ({numero_da_troca}) - Décima primeira Marcha")

            case 12:  # Caso a marcha seja 12
                print(f"Marcha trocada para: ({numero_da_troca}) - Décima segunda Marcha")

            case _:  # Caso nenhum dos valores anteriores seja encontrado
                print("Ponto Morto! Escolha uma marcha")
    
        

    def __str__(self):  # Método especial usado quando o objeto é exibido como texto
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  # Retorna o nome da classe e seus atributos


#b1 = Bicicleta("vermelha", "caloi", 2022, 600,'Eletrica',10)  # Cria o objeto b1 a partir da classe Bicicleta
#b1.buzinar()  # Chama o método buzinar do objeto b1
#b1.correr()  # Chama o método correr do objeto b1
#b1.parar()  # Chama o método parar do objeto b1
#print(b1.cor, b1.modelo, b1.ano, b1.valor)  # Exibe os atributos do objeto b1

#b2 = Bicicleta("verde", "monark", 2000, 189,'Hibrida',6)  # Cria o objeto b2 a partir da classe Bicicleta
#print(b2)  # Exibe o objeto b2 utilizando o método __str__
#b2.correr()  # Chama o método correr do objeto b2


b3 = Bicicleta("Branca","Tesla",2026,20599.90,"Hibrida",12) # Cria o objeto b3 a partir da classe Bicicleta
b3.revisao()  # Chama o método correr do objeto b3
b3.trocar_marcha('R')
print(b3.cor, b3.modelo) # Exibe os atributos do objeto b3



### Observações importantes


# OBSERVAÇÃO 1:
# Bicicleta é uma CLASSE.
# Ela funciona como um molde para criar objetos.

# OBSERVAÇÃO 2:
# b1 e b2 são OBJETOS da classe Bicicleta.
# Também podemos dizer que são INSTÂNCIAS da classe.

# OBSERVAÇÃO 3:
# cor, modelo, ano e valor são ATRIBUTOS.
# Eles representam as características da bicicleta.

# OBSERVAÇÃO 4:
# buzinar(), parar() e correr() são MÉTODOS.
# Eles representam comportamentos da bicicleta.

# OBSERVAÇÃO 5:
# __init__ é um MÉTODO ESPECIAL chamado automaticamente
# quando criamos um novo objeto.

# OBSERVAÇÃO 6:
# self representa o PRÓPRIO OBJETO.
# Por exemplo:
# self.cor = cor
# significa que o objeto recebe um atributo chamado cor.

# OBSERVAÇÃO 7:
# __str__ é um MÉTODO ESPECIAL.
# Ele define o que será mostrado quando fazemos:
# print(b2)

# OBSERVAÇÃO 8:
# __dict__ permite acessar os atributos do objeto
# em formato de dicionário.

# OBSERVAÇÃO 9:
# __

