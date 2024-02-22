'''Desenvolva um programa que leia 3 retas e diga se elas podem formar um triângulo'''

r1 = float(input('Digite o 1 número: '))
r2 = float(input('Digite o 2 número: '))
r3 = float(input('Digite o 3 número: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Esses valores {:.2f}, {:.2f} e {:.2f} formam um TRIÂNGULO'.format(r1,r2,r3))
else:
    print('Esses valores {:.2f}, {:.2f} e {:.2f} não formam um triângulo.'.format(r1,r2,r3))
