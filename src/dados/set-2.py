conjunto_1 = {1, 2, 3}
conjunto_2 = {3, 4, 5}

# union() -> Retorna a união de dois conjuntos
uniao = conjunto_1.union(conjunto_2)
print(uniao)

# intersection() -> Retorna a interseção de dois conjuntos
intersecao = conjunto_1.intersection(conjunto_2)
print(intersecao)

# difference() -> Retorna a diferença entre dois conjuntos
diferenca = conjunto_1.difference(conjunto_2)
print(diferenca)

# difference() -> Retorna a diferença entre dois conjuntos
diferenca = conjunto_2.difference(conjunto_1)
print(diferenca)

# update() -> Adiciona elementos de um conjunto a outro
conjunto_2.update({7, 5, 6})
print(conjunto_2)
