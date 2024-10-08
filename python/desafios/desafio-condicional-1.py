# Escreva um programa que pergunte a velocidade do carro
# de um usuário. Caso ultrapasse 80 km/h, exiba uma
# mensagem dizendo que o usuário foi multado.
# Nesse caso, exiba o valor da multa, cobrando R$5 por km
# acima de 80 km/h.

velocidade_carro = int(input("Informe a velocidade de carro: "))

velocidade_maxima = 80

if velocidade_carro > velocidade_maxima:
    print("Voce foi multado por estar acima de velocidade permitida (80km/h)")
    valor_multa = (velocidade_carro - velocidade_maxima) * 5
    print(f"O valor da multa é de R${valor_multa:.2f}")
else:
    print("Voce esta dentro do limite de velocidade permitida (80km/h)")
