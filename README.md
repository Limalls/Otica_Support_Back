# Ótica Support — API (Back-end)

API do sistema da **Ótica Support**: venda de óculos de sol e agendamento de consultas de vista. Este repositório contém apenas o back-end. O site da loja e o painel do dono ficam em repositórios separados e consomem esta API.

## Visão geral

| Repositório | Função |
|---|---|
| **Otica_Support_Back** (este) | API REST, regras de negócio e banco de dados |
| Front da loja | Site para clientes: catálogo, carrinho, checkout e agendamento |
| Painel do dono | Área restrita para acompanhar pedidos e consultas |

## Funcionalidades previstas (MVP)

- **Agendamento de consultas**: consulta de horários disponíveis, marcação, cancelamento e confirmação.
- **Catálogo de óculos**: listagem com filtros, detalhes do produto, estoque e imagens.
- **Carrinho e checkout**: criação de pedidos e pagamento (Pix/cartão).
- **Área administrativa**: login do dono, gestão de produtos, pedidos e consultas.

## Tecnologias

- Python 3.12+
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic (ORM e migrações)
- Pydantic (validação de dados)
- JWT (autenticação)
- Pytest (testes)

> A stack pode ser ajustada conforme o projeto evolui. Este README será atualizado junto com o código.

## Como rodar (em breve)

O passo a passo de instalação será adicionado quando a estrutura inicial do código for criada. De forma geral, será:

```bash
git clone https://github.com/Limalls/Otica_Support_Back.git
cd Otica_Support_Back
cp .env.example .env
# criar ambiente virtual, instalar dependências e iniciar o servidor
```

## Variáveis de ambiente

Todas as configurações ficam no arquivo `.env`. Use o `.env.example` como modelo. **Nunca envie o `.env` para o GitHub.**

## Estrutura planejada

```
Otica_Support_Back/
├── app/
│   ├── api/          # rotas (produtos, agendamentos, pedidos, auth)
│   ├── core/         # configurações e segurança
│   ├── models/       # modelos do banco de dados
│   ├── schemas/      # esquemas de entrada e saída (Pydantic)
│   └── services/     # regras de negócio
├── migrations/       # migrações do banco (Alembic)
├── tests/            # testes automatizados
└── docs/             # documentação adicional
```

## Contribuindo

Veja o [CONTRIBUTING.md](CONTRIBUTING.md) para o fluxo de trabalho e o padrão de commits.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE).
