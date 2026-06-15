# Breach Radar

API desenvolvida em Python/FastAPI para sincronização e consulta de breaches utilizando dados do Have I Been Pwned (HIBP).

---

## Tecnologias Utilizadas

* Python 3.11+
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* HTTPX
* Pytest
* Respx
* Ruff

---

## Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar ambiente virtual

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / MacOS**

```bash
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -e .
```

---

## Configuração do Banco de Dados

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=postgresql+psycopg://postgres:SUA_SENHA@localhost:5432/breach_radar
```

---

## Criar as Tabelas

Execute:

```bash
python create_tables.py
```

---

## Executando a Aplicação

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

## Endpoints

### Sincronizar Breaches

**POST**

```http
POST /sync
```

Exemplo de resposta:

```json
{
  "created": 1004,
  "updated": 0
}
```

---

### Listar Breaches

**GET**

```http
GET /breaches
```

#### Filtros disponíveis

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

Exemplo:

```http
GET /breaches?domain=adobe&page=1&page_size=20
```

---

### Buscar Breach por Nome

**GET**

```http
GET /breaches/{name}
```

Exemplo:

```http
GET /breaches/000webhost
```

---

## Testes

Executar todos os testes:

```bash
pytest -v
```

Resultado atual:

```text
24 passed
```

---

## Lint

Executar análise estática:

```bash
ruff check .
```

---

## Plano de Testes

O plano de testes está documentado em:

```text
TEST_PLAN.md
```

---

## Bug Hunt

Os bugs identificados, analisados e corrigidos encontram-se em:

```text
legacy/BUGS_FOUND.md
```

Os testes referentes ao Bug Hunt encontram-se em:

```text
tests/test_breach_matcher.py
```

---

## Funcionalidades Implementadas

### API

* Sincronização de breaches a partir do feed HIBP
* Persistência em PostgreSQL
* Consulta individual de breach
* Listagem paginada
* Filtros avançados
* Validação de parâmetros
* Validação de slug de breach

### Qualidade

* Testes automatizados
* Testes de paginação
* Testes de filtros
* Testes de validação
* Testes de timeout
* Testes de idempotência
* Bug Hunt com correções documentadas

---

## Autor

André Machado
