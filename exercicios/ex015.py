#Desenvolva um programa que pergunte ao usuario a quantidade de KM percorrido por carro alugado
#E a quantidade de dia alugados. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia
#E R$ 0.15 por KM rodado.
dias_alugados = int(input('Quantos dias será alugado o veículo ?'))
km_percorrido = float(input('Quantos KM serão percorridos ?'))

dias = 60.00 * dias_alugados
km = 0.15 * km_percorrido

total = dias + km

print('Total a pagar: {:.2f}'.format(total))

