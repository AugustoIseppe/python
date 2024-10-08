# Criando uma tupla
# A principal característica da tupla é que ela é imutável, ou seja, não é possível alterar seus valores. Diferente de uma lista, que é mutável.
tupla = (1, 2, 3, 4, 5, 2, 2)

# Métodos disponíveis para as tuplas

# count() -> Retorna a quantidade de vezes que um elemento aparece na tupla
print(tupla.count(2))  # Saída: 3

# index() -> Retorna o índice da primeira ocorrência de um elemento
print(tupla.index(5))  # Saída: 4

# len() -> Retorna o tamanho da tupla
print(len(tupla))  # Saída: 7

# max() -> Retorna o maior valor da tupla
print(max(tupla))  # Saída: 5

# min() -> Retorna o menor valor da tupla
print(min(tupla))  # Saída: 1

# sorted() -> Retorna uma NOVA tupla ordenada, mantendo a original inalterada
print(sorted(tupla))  # Saída: (1, 2, 2, 2, 3, 4, 5)

# sum() -> Retorna a soma dos elementos da tupla
print(sum(tupla))  # Saída: 19

# all() -> Retorna True se todos os elementos da tupla forem verdadeiros
print(all(tupla))  # True se todos os elementos da tuplas forem verdadeiros
