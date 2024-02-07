#Faça um programa que leiaum numero qualquer e mostre na tela seu Seno, Cosseno e Tangente

import math

an = float(input('Digite o ângulo que você deseja:'))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem\n'
      'SENO de {:.2f}\n'
      'COSSENO de {:.2f}\n'
      'TANGENTE de {:.2f}'
      .format(an, sen, cos, tan))

