class Pessoa:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Instanciando um objeto da classe Pessoa
p1 = Pessoa("Bia", 34)
p1.nome = "Pedro"
print(p1.nome, p1.idade)

# Instanciando outro objeto da classe Pessoa
p2 = Pessoa("Ana", 29)
print(p2.nome, p2.idade)
