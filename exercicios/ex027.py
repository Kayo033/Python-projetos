'''Desenvolva um programa que leia o nome de uma pessoa e mostre
1- O nome completo
2- O primeiro nome
3- O último nome'''

nome = str(input('Digite seu nome: ')).strip()

print('Prazer em te conhecer, {}'.format(nome))
print('O seu primeiro nome é {}'.format(nome.split()[0]))
print('O seu último nome é {}'.format(nome.split()[-1]))

