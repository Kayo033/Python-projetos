'''Criar um programa que pergunte a distância da viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM
para viagens de até 200 KM e R$ 0,45 para viagens mais longas.'''

distancia = float(input('Digite a distância da viagem em KM:'))

if distancia <= 200:
    kmValor = distancia * 0.50
else:
    kmValor = distancia * 0.45

print('O valor da sua passagem será de R${:.2f}'.format(kmValor))
