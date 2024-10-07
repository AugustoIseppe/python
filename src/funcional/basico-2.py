# Programacao funcional é um paradigma de programação, assim como a programação orientada a objetos e a programação procedural.
# Focando no uso de funções como "cidadãos de primeira classe" e enfatizando conceitos como imutabilidade e funções puras.
# Programação Funcional (PF):
# Funções puras: Funções que, dado o mesmo input, sempre retornam o mesmo output e não produzem efeitos colaterais (não alteram o estado externo).
# Imutabilidade: Variáveis e dados são imutáveis, ou seja, uma vez definidos, não podem ser modificados.
# Cidadãos de primeira classe: Funções são tratadas como valores, podendo ser passadas como argumentos, retornadas de outras funções ou atribuídas a variáveis.
# Funções de ordem superior: Funções que podem receber outras funções como argumentos ou retorná-las.
# Recursão: Recursão é preferida no lugar de loops.
# Desacoplamento: O estado e os dados são separados das funções que os manipulam.

def somar(a):
    def finalizar_soma(b):
        return a + b
    return finalizar_soma


print(somar(3)(4))

SALARIO_BASE = 2113.88
somar_com_salario_base = somar(SALARIO_BASE)

print(somar_com_salario_base(326.12))
print(somar_com_salario_base(444.12))
