# Otica Support Back

API do Otica Support, construída com **FastAPI**, **SQLAlchemy** e **PostgreSQL**.

## Estrutura

```
app/
├── api/        # rotas (routers) da API
├── core/       # configurações (.env) e conexão com o banco
├── models/     # models SQLAlchemy
├── schemas/    # schemas Pydantic
├── services/   # regras de negócio
└── main.py     # criação da aplicação FastAPI
alembic/        # migrações
tests/          # testes com Pytest
```

## Pré-requisitos

- Python 3.11+
- Docker e Docker Compose

## Como rodar

```bash
# 1. Clonar e entrar na pasta
git clone https://github.com/Limalls/Otica_Support_Back.git
cd Otica_Support_Back

# 2. Criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Configurar as variáveis de ambiente
cp .env.example .env             # Windows: copy .env.example .env

# 5. Subir o PostgreSQL
docker compose up -d

# 6. Aplicar as migrações
alembic upgrade head

# 7. Iniciar a API
uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Documentação (Swagger): http://localhost:8000/docs
- Health check: http://localhost:8000/health → `{"status": "ok"}`

## Variáveis de ambiente

| Variável       | Descrição                                      | Exemplo                                                          |
|----------------|------------------------------------------------|------------------------------------------------------------------|
| `DATABASE_URL` | String de conexão com o PostgreSQL             | `postgresql+psycopg2://postgres:postgres@localhost:5432/otica_support` |
| `CORS_ORIGINS` | Origens permitidas, separadas por vírgula      | `http://localhost:3000,http://localhost:5173`                    |
| `DEBUG`        | Modo debug                                     | `true`                                                           |

## Testes

```bash
pytest
```

## Migrações (Alembic)

```bash
# Criar uma nova migração a partir dos models
alembic revision --autogenerate -m "descricao da mudanca"

# Aplicar
alembic upgrade head

# Reverter a última
alembic downgrade -1
```

> Ao criar um novo model, importe-o em `app/models/__init__.py` para o Alembic detectá-lo.
