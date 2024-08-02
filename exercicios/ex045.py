from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Digite sua opção: '))

print('-=' * 12)
print(f'Computador jogou {computador}')
print(f'Jogador jogou {jogador}')
print('-=' * 12)

if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR vence')
    elif jogador == 2:
        print('COMPUTADOR vence')
    else:
        print('Jogada invalida')
elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR vence')
    else:
        print('JOGADA invalida')
elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR vence')
    elif jogador == 1:
        print('COMPUTADOR vence')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA invalida')
