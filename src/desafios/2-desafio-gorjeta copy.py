"""
Solicite ao usuario o total de uma conta e a porcentagem de gorjeta que ele deseja pagar.
Calcule e mosrtre o valor total da conta incluindo a gorjeta.
"""

total_conta = input("Informe o total da conta: ")
total_conta_formatado = float(total_conta)

gorjeta = input("Quantos % voce gostaria de dar para a gorjeta do garçom?")
gorjeta_formatada = float(gorjeta)

valor_gorjeta = total_conta_formatado * (gorjeta_formatada / 100)

valor_total_conta = total_conta_formatado + valor_gorjeta

print(f"O valor total da conta, incluindo a gorjeta, é R$ {
      valor_total_conta:.2f}")
