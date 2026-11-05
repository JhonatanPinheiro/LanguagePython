
from pathlib import Path
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    create_engine, select, and_, or_, func, inspect,
    String, DateTime, Numeric, Integer, Boolean, ForeignKey,
    CheckConstraint, Index
)

from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship, Session
)

from models import Base, Cliente, Produto, ItemPedido, Pedido


# Identifica a pasta onde está o main.py
PASTA_PROJETO = Path(__file__).resolve().parent
# Define o caminho do banco de dados
CAMINHO_BANCO = PASTA_PROJETO / "datavendas.db"
# Cria a conexão com o banco SQLite
engine = create_engine(f"sqlite:///{CAMINHO_BANCO}")
# Cria as tabelas no banco de dados, caso ainda não existam
Base.metadata.create_all(engine)

# Confirmação visual de que a conexão foi configurada
print("Conexão OK!")
