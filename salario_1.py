"""

Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por 
hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
Entrada

O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, 
quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

"""

numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhada = int(input("Horas trabalhadas: "))
valor_por_hora = round(float(input("Valor recebido por hora: ")), 2)

salario = horas_trabalhada * valor_por_hora

print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")
