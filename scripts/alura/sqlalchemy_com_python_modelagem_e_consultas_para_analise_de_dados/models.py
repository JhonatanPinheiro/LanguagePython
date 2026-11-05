
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    String,
    DateTime,
    Numeric,
    Boolean,
    ForeignKey,
    CheckConstraint,
    Index
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)


# Classe base para os modelos do banco de dados
class Base(DeclarativeBase):
    pass


# Modelo de clientes
class Cliente(Base):
    __tablename__ = "tb_clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    cidade: Mapped[str] = mapped_column(String(80), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)
    data_cadastro: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Relacionamento: um cliente pode ter vários pedidos
    pedidos: Mapped[list["Pedido"]] = relationship(back_populates="cliente")

    def __repr__(self) -> str:
        return f"Cliente(id={self.id}, nome='{self.nome}')"


# Modelo de produtos
class Produto(Base):
    __tablename__ = "tb_produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    categoria: Mapped[str] = mapped_column(String(100), nullable=False)
    preco_atual: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Relacionamento: um produto pode estar em vários itens de pedidos
    items: Mapped[list["ItemPedido"]] = relationship(back_populates="produto")

    def __repr__(self) -> str:
        return f"Produto(id={self.id}, nome='{self.nome}', preco={self.preco_atual})"


# Modelo de pedidos
class Pedido(Base):
    __tablename__ = "tb_pedidos"

    __table_args__ = (
        CheckConstraint(
            "status IN ('Created', 'Paid', 'Sent', 'Cancelled')",
            name="ch_status_pedido"
        ),

        # SQLite não cria índices automaticamente para chaves estrangeiras
        Index("idx_pedidos_cliente", "cliente_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("tb_clientes.id"), nullable=False
    )
    data_pedido: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    valor_total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    # Relacionamentos com cliente e itens
    cliente: Mapped["Cliente"] = relationship(back_populates="pedidos")
    items: Mapped[list["ItemPedido"]] = relationship(back_populates="pedido")

    def __repr__(self) -> str:
        return f"Pedido(id={self.id}, data='{self.data_pedido}', valor={self.valor_total})"


# Modelo de itens dos pedidos
class ItemPedido(Base):
    __tablename__ = "tb_itens_pedidos"

    __table_args__ = (
        # Índices para otimizar consultas pelas chaves estrangeiras
        Index("idx_itens_pedido", "pedido_id"),
        Index("idx_itens_produto", "produto_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("tb_pedidos.id"), nullable=False
    )

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("tb_produtos.id"), nullable=False
    )

    quantidade: Mapped[int] = mapped_column(nullable=False)
    preco_venda: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    # Relacionamentos com pedido e produto
    pedido: Mapped["Pedido"] = relationship(back_populates="items")
    produto: Mapped["Produto"] = relationship(back_populates="items")

    def __repr__(self) -> str:
        return (
            f"ItemPedido(pedido_id={self.pedido_id}, "
            f"produto_id={self.produto_id}, "
            f"quantidade={self.quantidade})"
        )
