import csv  # Importa a biblioteca para trabalhar com arquivos CSV
import json  # Importa a biblioteca para trabalhar com arquivos JSON

total = 0  # Cria uma variável para armazenar a soma das idades


# Etapa 1: Importar Dados

# Abre o arquivo pessoas.csv no modo leitura.
# O "r" indica que o arquivo será aberto para leitura.
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\pessoas.csv",
    "r"
) as arquivo:

    # Cria um leitor para percorrer as linhas do arquivo CSV.
    leitor = csv.reader(arquivo)

    # Pula a primeira linha do arquivo, que contém o cabeçalho.
    next(leitor)


    # Etapa 2: Processar Dados

    # Percorre cada linha do arquivo CSV.
    for linha in leitor:

        # Pega a idade que está na segunda coluna e transforma em número decimal.
        valor = float(linha[1])

        # Adiciona a idade encontrada ao total.
        total += valor


# Etapa 3: Gerar Relatório

# Cria um dicionário contendo a soma total das idades.
resultado = {
    "total_idade": total
}


# Etapa 4: Salvar Relatório

# Abre ou cria o arquivo relatorio_pipeline.json no modo escrita.
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\relatorio_pipeline.json",
    "w"
) as arquivo:

    # Converte o dicionário Python para JSON e salva no arquivo.
    json.dump(resultado, arquivo)


# Exibe uma mensagem informando que o pipeline foi executado.
print("Pipeline executado com sucesso")
