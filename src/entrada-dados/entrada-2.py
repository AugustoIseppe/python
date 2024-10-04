# O valor padrao do input é string, por isso é necessário converter para inteiro.

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

soma = int(num1) + int(num2)

print("A soma de", num1, "+", num2, "é", soma)
