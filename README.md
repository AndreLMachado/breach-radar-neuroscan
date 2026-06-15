Breach Radar

API desenvolvida em Python/FastAPI para sincronização e consulta de breaches utilizando dados do Have I Been Pwned (HIBP).

Tecnologias
Python 3.11+
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Pytest
Respx
HTTPX
Configuração do ambiente
Criar ambiente virtual
python -m venv .venv
Ativar ambiente virtual

Windows:

.venv\Scripts\activate

Linux/Mac:

source .venv/bin/activate
Instalar dependências
pip install -e .
Configuração do banco

Criar um arquivo .env na raiz do projeto:

DATABASE_URL=postgresql+psycopg://postgres:SUA_SENHA@localhost:5432/breach_radar
Executando a aplicação
uvicorn app.main:app --reload

A aplicação ficará disponível em:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs
Fluxo principal
Sincronizar breaches
POST /sync

Exemplo de resposta:

{
  "created": 1004,
  "updated": 0
}
Listar breaches
GET /breaches

Filtros disponíveis:

domain
data_class
breach_date_from
breach_date_to
added_date_from
added_date_to
min_pwn_count
max_pwn_count
is_verified
is_sensitive
is_spam_list
page
page_size
Buscar breach por nome
GET /breaches/{name}

Exemplo:

GET /breaches/000webhost
Executando os testes
pytest -v

Resultado atual:

23 passed
Bug Hunt

Os bugs identificados e corrigidos encontram-se em:

legacy/BUGS_FOUND.md
Plano de testes

O plano de testes está documentado em:

TEST_PLAN.md
