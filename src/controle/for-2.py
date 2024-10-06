print("Iterando uma LISTA:")
lista = [10, 20, 30, 40, 50]
lista_nomes = ["Maria", "João", "José", "Ana", "Pedro",
               "Carla", "Paulo", "Lucas", "Marta", "Carlos"]

for numero in lista:
    print(numero, end=" ")

for i, numero in enumerate(lista):
    print(f"({i}, {numero})", end=" ")

print("\n\nIterando uma TUPLA:")
tupla = (1, 2, 3, 4, 5)

for numero in tupla:
    print(numero, end=" ")

print("\n\nIterando um SET:")
conjunto = {1, 2, 3, 4, 5, 5, 5, 5, 5}

for numero in conjunto:
    print(numero, end=" ")

print("\n\nIterando um LISTA NOMES:")
for pessoas in lista_nomes:
    print(pessoas, end=" ")
