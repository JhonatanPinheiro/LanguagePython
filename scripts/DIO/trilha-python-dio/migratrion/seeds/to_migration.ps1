# PEGAR O DIRETÓRIO ATUAL 
# Obtém o caminho do diretório onde o script PowerShell está localizado.
$scriptDirectory = Split-Path $MyInvocation.MyCommand.Definition -Parent


# ARQUIVO DE SAÍDA COM TODOS OS SQL
# Cria o caminho completo do arquivo "migration.sql".
# Esse arquivo será utilizado para armazenar todos os comandos SQL.
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"


# VERIFICA SE O ARQUIVO JÁ EXISTE
# Test-Path verifica se o arquivo "migration.sql" já existe.
# Se o arquivo existir, ele será excluído antes de ser criado novamente.
if (Test-Path $outputFile) {

    # Remove o arquivo de saída existente.
    Remove-Item $outputFile
}


# PEGAR CONTEÚDO DOS ARQUIVOS
# Busca todos os arquivos que possuem a extensão ".sql"
# dentro do diretório onde o script está localizado.
#
# -Filter *.sql
#     Filtra somente arquivos com extensão .sql.
#
# -File
#     Garante que sejam retornados somente arquivos,
#     ignorando diretórios.
#
# Sort-Object Name
#     Organiza os arquivos em ordem alfabética pelo nome.
$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name


# CONCATENA ARQUIVOS
# Percorre cada arquivo SQL encontrado anteriormente.
foreach ($file in $sqlFiles) {

    # Lê todo o conteúdo do arquivo atual
    # e adiciona esse conteúdo ao final do arquivo "migration.sql".
    #
    # -Append
    #     Adiciona o conteúdo ao final do arquivo,
    #     sem sobrescrever o conteúdo anterior.
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile


    # Adiciona "GO" ao final de cada arquivo SQL.
    #
    # "GO" é utilizado como separador entre blocos de comandos SQL,
    # indicando o final do lote de comandos anterior.
    "GO" | Out-File -Append -FilePath $outputFile
}


# EXIBE UMA MENSAGEM NO CONSOLE
# Informa ao usuário que todos os arquivos SQL foram
# combinados no arquivo de saída.
#
# $outputFile contém o caminho completo do arquivo "migration.sql".
Write-Host "Todos os arquivos foram combinados em" $outputFile
