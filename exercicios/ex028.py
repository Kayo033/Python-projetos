'''Escreva um programa que faça o computador 'pensar' em um numero aleatorio inteiro de 0 à 5
e depois diga se o usuario perdeu ou ganhou'''

import random
from time import sleep
print('-=' * 30)
print('Tente adivinhar o número que estou pensando de 1 à 5...')
print('-=' * 30)
print('')

num_aleatorio = random.randint(1, 5)
numero_jogador = int(input('Em que número estou pensando 1 à 5: '))

print('Processando...')
sleep(2)

if numero_jogador == num_aleatorio:
    print('Parabéns você ganhou :), estava pensando no numero {} e você pensou no {}'.format(num_aleatorio, numero_jogador))
else:
    print('Eu ganhei :), estava pensando no numero {}'.format(num_aleatorio))
print('')
print('-=' * 7)
print('     FIM !')
print('-=' * 7)
