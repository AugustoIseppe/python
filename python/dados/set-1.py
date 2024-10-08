# Set é uma coleção não ordenada e sem elementos duplicados.
# O set nao aceita repetição de elementos.
# O set nao é indexado, ou seja, não é possível acessar seus elementos por índices.

frutas = {"banana", "maçã", "laranja", "banana"}
print(frutas)

# Adicionando um novo item ao set
frutas.add("uva")
print(frutas)

# Removendo um item do set
frutas.remove("banana")
print(frutas)

# Método len() -> Retorna o tamanho do set
print(len(frutas))

frutas.clear()
print(frutas)
