# A principal característica da tupla é que ela é imutável, ou seja, não é possível alterar seus valores. Diferente de uma lista, que é mutável.
# A tupla tambem é uma estrutura indexada, ou seja, é possível acessar seus valores através de um índice.
numeros = (1, 2, 3, 4, 5)

# Aceita valores através de índices
print(numeros)
print(numeros[0])
print(numeros[2])
# print(numeros[10]) # Erro!


misto = ("a", "b", "c", 7)
print(misto)  # A tupla pode aceitar valores de tipos diferentes

print(len(misto))  # A propriedade len() retorna o tamanho da tupla

tupla = (1)
print(type(tupla))

tupla = (1,)
print(type(tupla))
