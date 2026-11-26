from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True, index=True)
    telefone: Mapped[str | None] = mapped_column(String(30))

    agendamentos: Mapped[list["Agendamento"]] = relationship(  # noqa: F821
        back_populates="cliente", cascade="all, delete-orphan"
    )
    pedidos: Mapped[list["Pedido"]] = relationship(back_populates="cliente")  # noqa: F821
