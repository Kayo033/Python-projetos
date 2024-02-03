#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis sobre ele

n = input('Digite algo:')

print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Tem espaços? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É alfabético? {}'.format(n.isalpha()))
print('É alfanúmerico? {}'.format(n.isalnum()))
print('Está em maiúsculas? {}'.format(n.isupper()))
print('Está em minúscula? {}'.format(n.islower()))
print('Está capitalizada ()? {}'.format(n.istitle()))