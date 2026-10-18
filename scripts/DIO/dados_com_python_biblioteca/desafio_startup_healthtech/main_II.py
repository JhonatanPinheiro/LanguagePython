'''
Desafio
Em uma startup de HealthTech, você faz parte da equipe responsável por monitorar a saúde de pacientes usando dispositivos inteligentes. Cada paciente possui um arquivo de texto simples, onde o dispositivo registra diariamente a quantidade de passos dados. Para facilitar o acompanhamento, a equipe médica precisa de um programa que leia o arquivo de um paciente e retorne o total de passos registrados. Seu desafio é automatizar essa tarefa, garantindo que a soma seja feita corretamente mesmo que o arquivo contenha linhas vazias ou valores não numéricos (que devem ser ignorados).

Implemente um programa que leia o conteúdo de um arquivo texto (fornecido como uma string, onde cada linha representa um registro diário de passos). O programa deve somar apenas os valores numéricos inteiros presentes em cada linha, ignorando linhas vazias ou com dados inválidos. O resultado deve ser a soma total dos passos válidos encontrados no arquivo.

Entrada
Uma string representando o conteúdo de um arquivo texto, com cada linha separada por um caractere de nova linha (\n). Cada linha pode conter um número inteiro positivo, estar vazia ou conter texto não numérico.

Saída
Um único número inteiro representando a soma total dos passos válidos registrados no arquivo.

Exemplos
A tabela abaixo apresenta exemplos de entrada e saída:

Entrada	Saída
1000\n2000\n3000	6000
1500\nabc\n\n2500	4000
\n\n\n	0
steps\n500\n-100\n100	600

'''

# Lê o conteúdo do "arquivo" como uma única string da entrada padrão
file_content = input()

# Inicializa o total de passos válidos
total_steps = 0

# Converte o texto "\n" em quebras de linha reais
file_content = file_content.replace('\\n', '\n')

# Percorre cada linha do arquivo (cada registro diário)
for line in file_content.split('\n'):
    line = line.strip()

    # Se a linha estiver vazia, ignora
    if not line:
        continue

    # Tenta converter a linha para um número inteiro
    try:
        passos = int(line)

        # Soma somente os números inteiros positivos
        if passos > 0:
            total_steps += passos

    except ValueError:
        continue  # Ignora valores não numéricos

# Exibe o total de passos válidos
print(total_steps)
