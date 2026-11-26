from decimal import Decimal

from sqlalchemy import Boolean, Integer, Numeric, String, Text, true
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    descricao: Mapped[str | None] = mapped_column(Text)
    preco: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    estoque: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    categoria: Mapped[str | None] = mapped_column(String(80), index=True)
    imagem_url: Mapped[str | None] = mapped_column(String(500))
    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=true())

    itens_pedido: Mapped[list["ItemPedido"]] = relationship(back_populates="produto")  # noqa: F821
