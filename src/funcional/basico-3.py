# Programacao funcional é um paradigma de programação, assim como a programação orientada a objetos e a programação procedural.
# Focando no uso de funções como "cidadãos de primeira classe" e enfatizando conceitos como imutabilidade e funções puras.
# Programação Funcional (PF):
# Funções puras: Funções que, dado o mesmo input, sempre retornam o mesmo output e não produzem efeitos colaterais (não alteram o estado externo).
# Imutabilidade: Variáveis e dados são imutáveis, ou seja, uma vez definidos, não podem ser modificados.
# Cidadãos de primeira classe: Funções são tratadas como valores, podendo ser passadas como argumentos, retornadas de outras funções ou atribuídas a variáveis.
# Funções de ordem superior: Funções que podem receber outras funções como argumentos ou retorná-las.
# Recursão: Recursão é preferida no lugar de loops.
# Desacoplamento: O estado e os dados são separados das funções que os manipulam.

def remover_nome(nome):
    def remover_na_lista(lista):
        return [n for n in lista if n != nome]
    return remover_na_lista


remover_maria = remover_nome("Maria")
remover_joao = remover_nome("João")

lista_1 = ["Ana", "Pedro", "Maria", "João", "Maria"]
lista_2 = ["Guilherme", "Rebeca", "Maria", "Xico", "Tereza"]

print(remover_maria(lista_1))
print(remover_joao(lista_1))
print(remover_maria(lista_2))
print(remover_joao(lista_2))
print(remover_nome("Rebeca")(lista_2))
