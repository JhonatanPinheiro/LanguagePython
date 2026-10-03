def exibir_poema(data_extenso, *args, **kwargs):  # Define a função: data_extenso é obrigatório, *args recebe vários argumentos e **kwargs recebe argumentos nomeados
    texto = "\n".join(args)  # Junta todos os textos de *args, colocando uma quebra de linha entre eles
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])  # Percorre os kwargs e cria "Chave: Valor" para cada item
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"  # Monta a mensagem final juntando data, texto e metadados
    print(mensagem)  # Exibe a mensagem completa


exibir_poema(  # Chama a função

    "Sexta-Feira, 26 de Agosto 2026",  # Vai para data_extenso

    "Zen of Python",  # Vai para *args
    "Beautiful is better than ugly.",  # Vai para *args
    "Explicit is better than implicit.",  # Vai para *args
    "Simple is better than complex.",  # Vai para *args
    "Complex is better than complicated.",  # Vai para *args
    "Flat is better than nested.",  # Vai para *args
    "Sparse is better than dense.",  # Vai para *args
    "Readability counts.",  # Vai para *args
    "Special cases aren't special enough to break the rules.",  # Vai para *args
    "Although practicality beats purity.",  # Vai para *args
    "Errors should never pass silently.",  # Vai para *args
    "Unless explicitly silenced.",  # Vai para *args
    "In the face of ambiguity, refuse the temptation to guess.",  # Vai para *args
    "There should be one-- and preferably only one --obvious way to do it.",  # Vai para *args
    "Although that way may not be obvious at first unless you're Dutch.",  # Vai para *args
    "Now is better than never.",  # Vai para *args
    "Although never is often better than *right* now.",  # Vai para *args
    "If the implementation is hard to explain, it's a bad idea.",  # Vai para *args
    "If the implementation is easy to explain, it may be a good idea.",  # Vai para *args
    "If the implementation is easy to explain, it may be a good idea.",  # Vai para *args
    "Namespaces are one honking great idea -- let's do more of those!",  # Vai para *args

    autor="Tim Peters",  # Vai para **kwargs como chave "autor" e valor "Tim Peters"
    ano=1999,  # Vai para **kwargs como chave "ano" e valor 1999
    
)


# Observação: *args recebe vários argumentos posicionais como uma tupla, enquanto **kwargs recebe vários argumentos nomeados como um dicionário.
'''
| Recurso    | Recebe                                  | Dentro da função vira | Exemplo                         |
| ---------- | --------------------------------------- | --------------------- | ------------------------------- |
| `*args`    | Argumentos **posicionais**              | `tuple`               | `funcao(10, 20, 30)`            |
| `**kwargs` | Argumentos **nomeados** (`chave=valor`) | `dict`                | `funcao(nome="Jhow", idade=30)` |
'''


'''
A frase mais simples possível:

*args = vários valores.
**kwargs = várias informações com nome.
'''