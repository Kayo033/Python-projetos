'''Pergunte ao usuario um número, e diga se ele é PAR ou IMPAR'''

n1 = int(input('Digite um número: '))

if n1 % 2 == 0:
    print('O número {} é PAR !'.format(n1))
else:
    print('O número {} é IMPAR !'.format(n1))
