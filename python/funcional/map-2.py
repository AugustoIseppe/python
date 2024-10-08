lista_nomes = ["Ana", "Pedro", "Maria", "João", "Maria"]

# A funcao map() recebe os argumentos: uma funcao e uma lista.
r1 = map(lambda nome: nome[0], lista_nomes)

print(lista_nomes)
print(list(r1))
