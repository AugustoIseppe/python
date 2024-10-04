# Solicite ao usuário o raio de um círculo e calcule
# a área (`A = πr²`) e o volume de uma esfera com esse 
# raio (`V = 4/3πr³`).
# Use 3.14159 como aproximação de π.

PI = 3.14159
raio = float(input("Informe o valor do raio: "))

area = PI * (raio ** 2)
volume = 4 / 3 * PI * (raio ** 3)

print(f"A área é {area} m2 e o volume é {volume} m3.")
