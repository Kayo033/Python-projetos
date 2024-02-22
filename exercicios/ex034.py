#Faça um programa que leia o salario de uma pessoa e caso o salario foi maior que R$ 1.250 ele ganhará apenas 10%
#De aumento. Caso o salario seja abaixo de R$ 1.250 ele ganhará 15% de aumento

salario = float(input('Digite o seu salario: '))

salario_base = 1250

if salario <= salario_base:
    valor_soma = salario * 0.15
    novo_salario = salario + valor_soma
    print('Seu novo salario será de R${:.2f}'.format(novo_salario))
if salario > salario_base:
    valor_soma = salario * 0.10
    novo_salario = salario + valor_soma
    print('O seu novo salario será de R${:.2f}'.format(novo_salario))
