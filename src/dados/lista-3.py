numeros = [10, 20, 30]
indice_20 = numeros.index(20)  # Retorna o índice do elemento 20
print(indice_20)  # Saída: 1

numeros.append(10)
# Conta quantas vezes o número 10 aparece na lista
quantidade_10 = numeros.count(10)
print(quantidade_10)  # Saída: 2

numeros = [56, 32, 44, 4, -32, 7]
# Saída: [-32, 4, 7, 32, 44, 56] - ordena a lista em ordem crescente
numeros.sort()
print(numeros)

numeros.reverse()  # Inverte a ordem da lista em ordem decrescente
print(numeros)  # Saída: [56, 44, 32, 7, 4, -32]

numeros.clear()  # Remove todos os elementos da lista
print(numeros)  # Saída: []
