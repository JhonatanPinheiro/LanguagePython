import logging
from datetime import datetime
from main_III_path import caminho_logs

def execucao_log():
    pasta_logs = caminho_logs()
    pasta_logs.mkdir(parents=True, exist_ok=True)

    data_atual = datetime.now().strftime("%d%m%Y")
    arquivo_log = pasta_logs / f"log_{data_atual}.log"

    logging.basicConfig(
        filename=str(arquivo_log),
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )

    logging.info("Script de automação iniciado!")
    print(f"Arquivo de log: {arquivo_log}")