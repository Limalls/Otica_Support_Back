from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import StatusAgendamento


class Agendamento(Base):
    __tablename__ = "agendamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id", ondelete="CASCADE"), nullable=False, index=True
    )
    data_hora: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    status: Mapped[StatusAgendamento] = mapped_column(
        Enum(
            StatusAgendamento,
            name="status_agendamento",
            values_callable=lambda e: [m.value for m in e],
        ),
        nullable=False,
        default=StatusAgendamento.AGENDADO,
    )
    observacao: Mapped[str | None] = mapped_column(Text)

    cliente: Mapped["Cliente"] = relationship(back_populates="agendamentos")  # noqa: F821
