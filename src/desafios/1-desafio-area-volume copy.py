# Solicite ao usuario o raio de um círculo e calcule a sua área e o volume de uma esfera com esse raio.
# Volume da esfera = 4/3 * πr³ (quatro terços vezes pi vezes raio ao cubo)
# A=πr² (pi r ao quadrado)
# Use 3.14159 como valor de pi.

raio = input("Informe o raio de um círculo: ")
raio_formatado = float(raio)

PI = 3.14159

area = PI * (raio_formatado ** 2)
volume = 4/3 * PI * (raio_formatado ** 3)

print("A área do círculo é", area)
print("O volume da esfera é", volume)
