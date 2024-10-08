"""
Seu desafio é criar um programa que converta temperaturas de Celsius para Fahrenheit e vice-versa.
A fórmula para converter de Celsius para Fahrenheit é: F = C * (9/5) + 32
Solicite ao usuário que informe a temperatura e a unidade de origem e mostre o resultado da conversão.
"""

temperatura = input("Informe a temperatura em °C: ")
temperatura_formatada = float(temperatura)

f = temperatura_formatada * 9/5 + 32

print(f"A temperatura em Fahrenheit é {f:.2f}°F")
