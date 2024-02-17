#Abaixo CONDIÇÃO COMPOSTA
'''n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
n3 = float(input('Digite a 3 nota: '))
m = (n1 + n2 + n3) / 3

if m >= 6.0:
    print('Media: {:.2f}, aprovado !'.format(m))
else:
    print('Media: {:.2f}, reprovado !'.format(m))'''

#Abaixo CONDIÇÃO COMPOSTA SIMPLIFICADA
n1 = float(input('Digite a 1 nota: '))
n2 = float(input('Digite a 2 nota: '))
n3 = float(input('Digite a 3 nota: '))
m = (n1 + n2 + n3) / 3

print('A sua media foi de {:.2f}'.format(m))
print('PARABENS' if m >= 6 else 'REPROVADO')
