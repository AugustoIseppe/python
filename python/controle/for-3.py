funcionario = {
    "nome": "Maria",
    "salario": 7655.22,
    "idade": 35,
    "ativo": True,
}

for chave in funcionario:
    print(chave)
print("--------------------")
for chave in funcionario.keys():
    print(chave, "=>", funcionario[chave])
print("--------------------")

for valor in funcionario.values():
    print(valor)
print("--------------------")

for chave, valor in funcionario.items():
    print(chave, "=>", valor)
