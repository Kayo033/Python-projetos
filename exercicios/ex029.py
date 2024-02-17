'''Crie um programa que leia a velocidade de um usuario, e diga se ele ultrapassou a
via da pista ou não, e caso tenha ultrapassado será multado em R$ 280.00'''

velocidade_pista = 80.00
velocidade_usuario = float(input('Qual a velocidade do veículo? '))

if velocidade_usuario > velocidade_pista:
    velocidade_acima = (velocidade_usuario - velocidade_pista) * 7
    print('MULTADO, por ultrapassar o limite da via 80Km/h ! Você será multado em R$ {:.2f}'.format(velocidade_acima))
elif velocidade_usuario >= 76 and 79:
    print('No LIMITE da via cuidado ! Mas não será multado.')
else:
    print('NÃO será multado, velocidade de acordo com a via !')

print('Dirija com segurança !')
