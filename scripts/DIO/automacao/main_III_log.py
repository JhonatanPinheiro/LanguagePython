import logging  # Permite registrar mensagens de log
from datetime import datetime  # Permite obter a data e hora atual
from main_III_path import caminho_logs  # Importa o caminho da pasta de logs

def execucao_log():
    pasta_logs = caminho_logs()  # Obtém o caminho da pasta de logs
    pasta_logs.mkdir(parents=True, exist_ok=True)  # Cria a pasta se não existir

    data_atual = datetime.now().strftime("%d%m%Y")  # Formata a data: dia, mês e ano
    arquivo_log = pasta_logs / f"log_{data_atual}.log"  # Define o nome do arquivo

    logging.basicConfig(
        filename=str(arquivo_log),  # Define o arquivo que receberá os logs
        filemode="a",  # Acrescenta registros sem apagar os anteriores
        level=logging.INFO,  # Registra mensagens INFO e níveis superiores
        format="%(asctime)s - %(levelname)s - %(message)s",  # Formato das mensagens
        encoding="utf-8"  # Permite salvar caracteres acentuados
    )

    logging.info("Script de automação iniciado!")  # Registra o início do script
