# O Dictionary é uma coleção desordenada, mutável e indexada. Em Python, os dicionários são escritos com chaves e têm chaves e valores.
# Ela é semelhante ao Map em Dart.
funcionario = {
    "nome": "Augusto Iseppe",
    "idade": 31,
    "cidade": "Pirassununga",
    "ativo": True
}
# a funcao get() é mais segura que a notacao de colchetes
print(funcionario.get("nome"))

# print(funcionario["salario"])  # Erro!
print(funcionario.get("salario"))

# O segundo argumento é o valor padrão, caso a chave não exista
print(funcionario.get("salario", 0))

# A funcção keys() retorna uma lista com todas as chaves do dicionário
print(funcionario.keys())

# A função values() retorna uma lista com todos os valores do dicionário
print(funcionario.values())

# A função items() retorna uma lista de tuplas com chave e valor
print(funcionario.items())
