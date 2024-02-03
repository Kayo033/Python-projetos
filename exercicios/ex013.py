#Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário, com uma porcentagem de aumento.

salario_atual = float(input('Digite seu salario R$'))
aumento = float(input('Qual a porcentagem de aumento:'))

novo = salario_atual + (salario_atual * aumento / 100)

print('O seu novo salário com {:.2f}% de aumento, será de R${:.2f}'.format(aumento, novo))