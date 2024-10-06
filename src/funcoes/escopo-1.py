def exibir_nome():
    # Escopo Local
    nome_completo = f"Augusto {sobrenome}"
    print(nome_completo)


# Escopo Global
sobrenome = 'Iseppe'

exibir_nome()
# print(nome_completo)
