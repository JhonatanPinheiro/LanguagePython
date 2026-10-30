class Animal:  # Define a classe pai Animal

    def __init__(self, nro_patas):  # Método construtor da classe Animal
        self.nro_patas = nro_patas  # Cria o atributo nro_patas

    def __str__(self):  # Método especial utilizado quando o objeto é exibido como texto
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"  # Retorna o nome da classe e seus atributos


class Mamifero(Animal):  # Define Mamifero como classe filha de Animal

    def __init__(self, cor_pelo, **kw):  # Construtor que recebe cor_pelo e outros argumentos em **kw
        self.cor_pelo = cor_pelo  # Cria o atributo cor_pelo
        super().__init__(**kw)  # Chama o próximo construtor da cadeia de herança


class Ave(Animal):  # Define Ave como classe filha de Animal

    def __init__(self, cor_bico, **kw):  # Construtor que recebe cor_bico e outros argumentos em **kw
        self.cor_bico = cor_bico  # Cria o atributo cor_bico
        super().__init__(**kw)  # Chama o próximo construtor da cadeia de herança


class Gato(Mamifero):  # Define Gato como classe filha de Mamifero
    pass  # Não possui implementação própria e utiliza a implementação herdada


class Ornitorrinco(Mamifero, Ave):  # Define Ornitorrinco herdando de Mamifero e Ave

    def __init__(self, cor_bico, cor_pelo, nro_patas):  # Construtor próprio do Ornitorrinco
        
        #print(Ornitorrinco.__mro__) # Mostra a ordem de resolução de métodos (MRO) - Pode chamar dessa 1 Forma
        #print(Ornitorrinco.mro()) # Mostra a ordem de resolução de métodos (MRO) - Ou Pode chamar dessa 2 Forma
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)  # Passa os argumentos para a cadeia de herança


gato = Gato(nro_patas=4, cor_pelo="Preto")  # Cria um objeto da classe Gato
print(gato)  # Exibe o objeto gato utilizando o método __str__

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")  # Cria um objeto da classe Ornitorrinco
print(ornitorrinco)  # Exibe o objeto ornitorrinco utilizando o método __str__


# OBSERVAÇÕES IMPORTANTES:

# OBSERVAÇÃO 1:
# Animal é a CLASSE PAI.
#
# Mamifero e Ave herdam de Animal.

# OBSERVAÇÃO 2:
# Gato herda de Mamifero.
#
# Gato → Mamifero → Animal

# OBSERVAÇÃO 3:
# Ornitorrinco possui HERANÇA MÚLTIPLA.
#
# class Ornitorrinco(Mamifero, Ave)
#
# Isso significa que Ornitorrinco herda de duas classes:
# Mamifero e Ave.

# OBSERVAÇÃO 4:
# **kw permite receber vários argumentos nomeados
# que não foram definidos individualmente no parâmetro.
#
# Por exemplo:
# **kw

# OBSERVAÇÃO 5:
# Quando usamos:
#
# super().__init__(**kw)
#
# os argumentos armazenados em kw são enviados
# para o próximo __init__ da cadeia de herança.

# OBSERVAÇÃO 6:
# Mamifero recebe:
#
# cor_pelo
#
# e depois envia os demais argumentos para a próxima classe
# utilizando:
#
# super().__init__(**kw)

# OBSERVAÇÃO 7:
# Ave recebe:
#
# cor_bico
#
# e também envia os demais argumentos para a próxima classe
# utilizando:
#
# super().__init__(**kw)

# OBSERVAÇÃO 8:
# O Ornitorrinco possui características de Mamifero e Ave:
#
# cor_pelo
# cor_bico
# nro_patas

# OBSERVAÇÃO 9:
# Nesta linha:
#
# super().__init__(
#     cor_pelo=cor_pelo,
#     cor_bico=cor_bico,
#     nro_patas=nro_patas
# )
#
# os argumentos são encaminhados pela cadeia de herança.

# OBSERVAÇÃO 10:
# O Python utiliza a ORDEM DE RESOLUÇÃO DE MÉTODOS (MRO)
# para determinar qual classe será chamada pelo super().
#
# No caso do Ornitorrinco, a herança é:
#
# Ornitorrinco
# Mamifero
# Ave
# Animal
# object

# OBSERVAÇÃO 11:
# Gato utiliza pass porque não precisa de um
# __init__ próprio.
#
# Por isso, ele utiliza o __init__ herdado de Mamifero.

# OBSERVAÇÃO 12:
# __str__ está definido em Animal.
#
# Como as outras classes herdam de Animal,
# elas também podem utilizar esse método.

# OBSERVAÇÃO 13:
# self.__dict__ contém os atributos existentes no objeto.
#
# No Gato:
# cor_pelo
# nro_patas
#
# No Ornitorrinco:
# cor_pelo
# cor_bico
# nro_patas