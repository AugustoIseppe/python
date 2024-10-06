nome = """
Augusto Iseppe Balan
"""
meu_nome = "Darinha Iseppe Balan"
# A funcao split() retorna uma lista com as partes da string
partes_nome = nome.split()
meu_nome_em_partes = meu_nome.split()

for parte in meu_nome_em_partes:
    print(parte)

print(partes_nome)
print(meu_nome_em_partes)

match partes_nome:
    case [primeiro]:
        sigla = primeiro[0:2]
    # case [primeiro, segundo]:
    #     sigla = primeiro[0] + segundo[0]
    case [primeiro, *m, ultimo]:
        sigla = primeiro[0] + ultimo[0]
    case _:
        sigla = "AL"

print(f"A sigla do usuário é {sigla.upper()}")
