from app.models import Base


def test_tabelas_existem():
    assert set(Base.metadata.tables) == {
        "produtos",
        "clientes",
        "agendamentos",
        "pedidos",
        "itens_pedido",
        "usuarios",
    }


def _fks(tabela: str) -> set[str]:
    return {
        f"{fk.parent.name}->{fk.column.table.name}.{fk.column.name}"
        for fk in Base.metadata.tables[tabela].foreign_keys
    }


def test_chaves_estrangeiras():
    assert _fks("agendamentos") == {"cliente_id->clientes.id"}
    assert _fks("pedidos") == {"cliente_id->clientes.id"}
    assert _fks("itens_pedido") == {"pedido_id->pedidos.id", "produto_id->produtos.id"}


def test_status_enums():
    t = Base.metadata.tables
    assert t["agendamentos"].c.status.type.enums == [
        "agendado", "confirmado", "cancelado", "concluido",
    ]
    assert t["pedidos"].c.status.type.enums == [
        "pendente", "pago", "enviado", "entregue", "cancelado",
    ]
