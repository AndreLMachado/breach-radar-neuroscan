# Breach Radar

API desenvolvida em Python/FastAPI para sincronização e consulta de breaches utilizando dados do Have I Been Pwned (HIBP).

---

# Tecnologias Utilizadas

* Python 3.11+
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* HTTPX
* Pytest
* Respx
* Ruff
* Docker
* Docker Compose

---

# Configuração do Ambiente

## 1. Criar ambiente virtual

```bash
python -m venv .venv
```

## 2. Ativar ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / MacOS

```bash
source .venv/bin/activate
```

## 3. Instalar dependências

```bash
pip install -e .
```

---

# Configuração do Banco de Dados

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg://postgres:SUA_SENHA@localhost:5432/breach_radar
```

---

# Criar as Tabelas

Execute:

```bash
python create_tables.py
```

---

# Executando a Aplicação Localmente

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Executando com Docker

## Subir aplicação e banco

```bash
docker compose up --build
```

A API ficará disponível em:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

## Parar containers

```bash
docker compose down
```

## Remover volumes do banco

```bash
docker compose down -v
```

---

# Endpoints

## Sincronizar Breaches

**POST**

```http
POST /sync
```

### Exemplo de resposta

```json
{
  "created": 1004,
  "updated": 0
}
```

---

## Listar Breaches

**GET**

```http
GET /breaches
```

### Filtros disponíveis

| Parâmetro        | Descrição                               |
| ---------------- | --------------------------------------- |
| domain           | Filtra por domínio                      |
| data_class       | Filtra por classe de dados              |
| breach_date_from | Data inicial do breach                  |
| breach_date_to   | Data final do breach                    |
| added_date_from  | Data inicial de inclusão                |
| added_date_to    | Data final de inclusão                  |
| min_pwn_count    | Quantidade mínima de registros expostos |
| max_pwn_count    | Quantidade máxima de registros expostos |
| is_verified      | Apenas breaches verificados             |
| is_sensitive     | Apenas breaches sensíveis               |
| is_spam_list     | Apenas listas de spam                   |
| page             | Página                                  |
| page_size        | Quantidade por página                   |

### Exemplo

```http
GET /breaches?domain=adobe&page=1&page_size=20
```

---

## Buscar Breach por Nome

**GET**

```http
GET /breaches/{name}
```

### Exemplo

```http
GET /breaches/000webhost
```

---

# Testes

Executar todos os testes:

```bash
pytest -v
```

Resultado atual:

```text
24 passed
```

> Atualize para 25 passed caso o teste adicional de filtros combinados esteja incluído e passando.

---

# Lint

Executar análise estática:

```bash
ruff check .
```

---

# Plano de Testes

O plano de testes está documentado em:

```text
TEST_PLAN.md
```

---

# Bug Hunt

Os bugs identificados, analisados e corrigidos encontram-se em:

```text
legacy/BUGS_FOUND.md
```

Os testes referentes ao Bug Hunt encontram-se em:

```text
tests/test_breach_matcher.py
```

---

# Funcionalidades Implementadas

## API

* Sincronização de breaches a partir do feed HIBP
* Persistência em PostgreSQL
* Consulta individual de breach
* Listagem paginada
* Filtros avançados
* Validação de parâmetros
* Validação de slug de breach

## Infraestrutura

* Docker
* Docker Compose
* PostgreSQL containerizado
* Inicialização automática das tabelas

## Qualidade

* Testes automatizados
* Testes de integração
* Testes de paginação
* Testes de filtros
* Testes de validação
* Testes de timeout
* Testes de idempotência
* Bug Hunt com correções documentadas

---

# Extras Implementados

* Docker
* Docker Compose
* Bug Hunt com correções documentadas
* Testes automatizados
* Testes de integração
* Testes de idempotência
* Testes de timeout
* Validação de entrada
* Paginação
* Filtros avançados

---

# Estrutura do Projeto

```text
app/
├── api/
├── clients/
├── models/
├── repositories/
├── schemas/
├── services/

tests/
├── test_assets.py
├── test_breaches.py
├── test_sync.py
├── test_breach_matcher.py

legacy/
├── BUGS_FOUND.md
├── breach_matcher.py

Dockerfile
docker-compose.yml
README.md
TEST_PLAN.md
```

---

# Autor

André Machado
