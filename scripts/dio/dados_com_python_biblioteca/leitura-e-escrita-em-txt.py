# r = leitura
# w = escrita (apaga o conteúdo antigo)
# a = adicionar conteúdo
# função open() = abre ou cria um arquivo

with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\dados.txt",
    "w"
) as arquivo:

    # função write() = escreve conteúdo no arquivo
    arquivo.write("Python é uma linguagem poderosa. \n")
    arquivo.write("Estamos aprendendo arquivos")


# Lendo o arquivo completo
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\dados.txt",
    "r"
) as arquivo:

    # função read() = lê todo o conteúdo do arquivo
    conteudo = arquivo.read()

    # Exibe o conteúdo do arquivo no terminal
    print(conteudo)


# Lendo o arquivo linha por linha
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\dados.txt",
    "r"
) as arquivo:

    # Percorre cada linha do arquivo
    for linha in arquivo:

        # função strip() = remove espaços e quebras de linha
        print(linha.strip())


# Cria o arquivo relatorio.txt
# O modo "w" cria o arquivo ou apaga o conteúdo antigo
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\relatorio.txt",
    "w"
) as arquivo:

    # Escreve o título do relatório
    arquivo.write("Relatorio de Vendas\n")

    # Escreve o total de vendas
    arquivo.write("Total: 1500")


# Abre o arquivo no modo "a" para adicionar conteúdo
# O conteúdo existente não será apagado
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\relatorio.txt",
    "a"
) as arquivo:

    # Adiciona uma nova informação ao final do arquivo
    arquivo.write("\nNovo registro adicionado.")