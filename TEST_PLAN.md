# Test Plan – Breach Radar

## Estratégia adotada

A estratégia de testes foi dividida em três frentes principais:

1. Testes de API usando `TestClient` do FastAPI.
2. Testes com mock do feed externo da HIBP usando `respx`.
3. Testes unitários do módulo legado `legacy/breach_matcher.py`.

O objetivo foi validar os principais fluxos funcionais, cenários negativos, regras de negócio e bugs plantados no código legado.

---

## Escopo testado

### Health Check

- `GET /health` retorna status `ok`.

### Assets

- Criação de asset com `POST /assets`.

### Breaches

Foram testados os principais endpoints:

- `GET /breaches`
- `GET /breaches/{name}`

Foram testados os seguintes filtros:

- `domain`
- `data_class`
- `is_verified`
- `min_pwn_count`
- `added_date_from`
- `added_date_to`

Também foram testados:

- Paginação com `page` e `page_size`.
- Breach existente.
- Breach inexistente.
- Nome de breach inválido retornando `400`.

### Sync

Foram testados:

- Sincronização com mock do feed da HIBP.
- Execução de `/sync` duas vezes sem duplicação.
- Timeout do feed da HIBP retornando erro controlado.

### Bug Hunt

Foram testados e corrigidos três bugs no arquivo legado `legacy/breach_matcher.py`:

1. `domain_matches` não era case-insensitive.
2. `within_breach_date` excluía a data final.
3. `paginate` retornava um item a menos que o esperado.

---

## Casos positivos

- API sobe corretamente.
- `/health` responde com sucesso.
- `/breaches` retorna lista paginada.
- `/breaches/{name}` retorna um breach existente.
- `/sync` persiste dados do feed mockado.
- Filtros retornam registros compatíveis.
- Paginação retorna páginas diferentes.
- Bug hunt corrigido com testes passando.

---

## Casos negativos

- Breach inexistente retorna `404`.
- Nome de breach inválido retorna `400`.
- `page` menor que 1 retorna `400`.
- `page_size` menor que 1 retorna `400`.
- `page_size` acima do limite retorna `400`.
- `min_pwn_count` negativo retorna `400`.
- Timeout do feed HIBP retorna erro controlado.

---

## Edge cases testados

- `/sync` executado duas vezes com o mesmo breach não duplica registros.
- Busca de domínio com diferença de maiúsculas/minúsculas no módulo legado.
- Filtro por data incluindo a data final no módulo legado.
- Paginação do módulo legado retornando exatamente o tamanho esperado.

---

## O que não foi testado e por quê

- Testes de carga/performance não foram incluídos por limitação de escopo do desafio.
- Testes end-to-end com uma instância real isolada de PostgreSQL em CI não foram configurados nesta versão.
- Testes para todos os filtros combinados possíveis não foram exaustivos para evitar redundância, mas há cobertura dos principais filtros isolados e da semântica de paginação.
- Docker, GitHub Actions e Alembic ficaram como melhorias futuras/opcionais.

---

## Riscos identificados

- Os testes atuais usam o banco configurado no `.env`, o que exige atenção para não rodar testes contra dados sensíveis ou ambiente produtivo.
- A estratégia atual de sync usa upsert em nível de aplicação; em cenários de alta concorrência, seria melhor usar `ON CONFLICT DO UPDATE` diretamente no PostgreSQL.
- O tratamento de payload inválido do feed pode ser fortalecido com validação formal por schemas Pydantic.
- A busca em `data_classes` usa cast textual sobre JSONB, funcionando para o desafio, mas podendo ser otimizada com consultas JSONB mais específicas.
