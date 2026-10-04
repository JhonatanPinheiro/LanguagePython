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