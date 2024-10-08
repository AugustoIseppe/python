"""
Peça ao usuário para inserir uma quantidade de kk e converta essa quantidade para milhas.
1 km = 0.621371 milhas
"""

km = float(input("Informe a quantidade de km: "))

MILES = 0.621371

km_to_milhas = km * MILES

print(f"{km} km é igual a {km_to_milhas:.2f} milhas")
