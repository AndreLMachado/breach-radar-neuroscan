Bugs Encontrados – breach_matcher.py
Bug 1 – domain_matches não era case-insensitive
Problema

O contrato informava que a busca por domínio deveria ser case-insensitive:

Exemplo:

query = "Dropbox"
Domain = "dropbox.com"

Deveria retornar True.

Entretanto a implementação fazia:

return query in domain

Como apenas o domínio era convertido para lowercase, consultas com letras maiúsculas falhavam.

Correção
return query.lower() in domain
Bug 2 – within_breach_date excluía a data final
Problema

O contrato informava que o intervalo deveria ser inclusivo:

[date_from, date_to]

Entretanto a implementação utilizava:

if date_to and bd >= date_to:
    return False

Isso fazia com que um breach ocorrido exatamente na data final fosse removido do resultado.

Correção
if date_to and bd > date_to:
    return False
Bug 3 – paginate retornava uma página incompleta
Problema

A implementação utilizava:

end = start + page_size - 1

Como o slice do Python já possui limite exclusivo, o último item da página era perdido.

Exemplo:

paginate([1,2,3,4,5], page=1, page_size=2)

Retornava:

[1]

Em vez de:

[1, 2]
Correção
end = start + page_size
