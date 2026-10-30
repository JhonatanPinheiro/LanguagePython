'''Desafio
Em uma startup de HealthTech, você foi contratado para ajudar a equipe de dados a organizar informações de pacientes vindas de arquivos externos. O sistema recebe arquivos de texto simples, onde cada linha contém o nome de um paciente seguido de sua idade, separados por uma vírgula. Seu objetivo é criar um programa que leia esse arquivo, encontre o paciente mais velho e retorne seu nome. Caso haja empate na idade, retorne o nome que aparece primeiro no arquivo. Se o arquivo estiver vazio ou não houver dados válidos, retorne "Nenhum paciente encontrado".

Implemente uma função que leia o conteúdo do arquivo (fornecido como uma string, com cada linha representando um registro), processe os dados conforme descrito e produza a saída correta. Não utilize bibliotecas externas, apenas recursos padrão da linguagem. Considere que os nomes não contêm vírgulas e que as idades são números inteiros positivos. Linhas mal formatadas devem ser ignoradas.

Entrada
Uma string representando o conteúdo de um arquivo de texto, onde cada linha contém um nome e uma idade separados por vírgula. Linhas podem estar vazias ou mal formatadas.

Saída
Uma string contendo o nome do paciente mais velho. Se não houver dados válidos, retorne "Nenhum paciente encontrado".

Exemplos
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	Saída
Lucas,34
Maria,28
Joao,45	Joao
Anna,50
Pedro,50
Carlos,40	Anna
Julia,abc
Marcos,27
,30	Marcos
 	Nenhum paciente encontrado
'''


# Entrada via input padrão: recebe o conteúdo do arquivo como uma string
file_content = input()

# Inicializa a variável que armazenará o nome do paciente mais velho
paciente_mais_velho = None

# Inicializa a variável que armazenará a maior idade encontrada
maior_idade = 0

# Substitui o texto "<br>" por uma quebra de linha, caso a entrada venha nesse formato
file_content = file_content.replace("<br>", "\n")

# Percorre cada linha do conteúdo, separando os registros pelas quebras de linha
for line in file_content.splitlines():

    # Remove espaços em branco do início e do final da linha
    line = line.strip()

    # Verifica se a linha está vazia
    if not line:
        continue  # Pula a linha vazia e passa para a próxima

    # Divide a linha em duas partes usando a vírgula como separador
    parts = line.split(',')

    # Verifica se a linha possui exatamente duas partes: nome e idade
    if len(parts) != 2:
        continue  # Ignora linhas mal formatadas

    # Armazena o nome e a idade em variáveis separadas, removendo espaços extras
    name, age_str = parts[0].strip(), parts[1].strip()

    # Verifica se o nome do paciente está vazio
    if not name:
        continue  # Ignora registros sem nome

    # Tenta converter a idade de texto para número inteiro
    try:
        age = int(age_str)

        # Verifica se a idade é menor ou igual a zero
        if age <= 0:
            continue  # Ignora idades inválidas

    # Captura o erro caso a idade não possa ser convertida para inteiro
    except ValueError:
        continue  # Ignora valores como "abc"

    # Verifica se a idade atual é maior que a maior idade encontrada
    if age > maior_idade:

        # Atualiza a maior idade encontrada
        maior_idade = age

        # Armazena o nome do paciente que possui essa idade
        paciente_mais_velho = name

# Verifica se algum paciente válido foi encontrado
if paciente_mais_velho is None:

    # Exibe esta mensagem se não houver pacientes válidos
    print("Nenhum paciente encontrado")

else:

    # Exibe o nome do paciente mais velho
    print(paciente_mais_velho)



# RESUMO DO CÓDIGO: OBJETIVO E FUNCIONAMENTO

# 1. ENTRADA:
# Recebe os dados dos pacientes em uma string.

# 2. TRATAMENTO:
# Substitui "<br>" por quebras de linha reais para separar os registros.

# 3. SEPARAÇÃO:
# Divide o conteúdo em linhas e cada linha em nome e idade.

# 4. VALIDAÇÃO:
# Ignora linhas vazias, registros mal formatados, nomes vazios,
# idades que não são números inteiros e idades menores ou iguais a zero.

# 5. COMPARAÇÃO:
# Compara a idade de cada paciente com a maior idade já encontrada.
# Se encontrar uma idade maior, atualiza a idade e o nome.
# Como utiliza ">", em vez de ">=", mantém o primeiro paciente em caso de empate.

# 6. RESULTADO:
# Exibe o nome do paciente mais velho.
# Se nenhum paciente válido for encontrado, exibe:
# "Nenhum paciente encontrado".

# OBJETIVO FINAL:
# Identificar o paciente mais velho de uma lista de registros,
# ignorando dados inválidos e respeitando a ordem original em caso de empate.
