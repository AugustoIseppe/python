# O Dictionary é uma coleção desordenada, mutável e indexada. Em Python, os dicionários são escritos com chaves e têm chaves e valores.
# Ela é semelhante ao Map em Dart.
funcionario = {
    "nome": "Augusto Iseppe",
    "idade": 31,
    "cidade": "Pirassununga",
    "ativo": True
}

# Atribuindo um novo valor a uma chave
funcionario["ativo"] = False
print(funcionario)

# Método update() -> Atualizando o dicionário (não precisa ter todas as chaves), apenas as que deseja atualizar
funcionario.update({
    "idade": 27,
    "ativo": True,
    "profissao": "Reporter"
})
print(funcionario)

# Método pop() -> Remove a chave e retorna o valor
cidade = funcionario.pop("cidade")
print(cidade)
print(funcionario)

# Método clear() -> Limpa o dicionário
funcionario.clear()
print(funcionario)
