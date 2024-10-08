# O Dictionary é uma coleção desordenada, mutável e indexada. Em Python, os dicionários são escritos com chaves e têm chaves e valores.
# Ela é semelhante ao Map em Dart.
funcionario = {
    "nome": "Augusto Iseppe",
    "idade": 31,
    "cidade": "Pirassununga",
    "ativo": True
}

print(funcionario["nome"])
print(funcionario["idade"])

# Adicionando um novo item ao dicionário
funcionario["profissão"] = "Desenvolvedor de Software"
print(funcionario["profissão"])
