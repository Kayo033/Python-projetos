#Crie um programa que leia um numero real / fracionado  qualquer pelo teclado e mostre na tela sua porção inteira

#No código abaixo a importação MATCH importa tudo da biblioteca
import math
# n1 = float(input('Digite um numero: '))
# #A função ROUND() é usada para arredondar o número de ponto flutuante numero para o inteiro mais próximo.
# n1_inteiro = round(n1)
# print(n1_inteiro)

#No código abaixo importamos apenas a função TRUNC da biblioteca MATCH
from math import trunc
n1 = float(input('Digite um numero: '))
n1_inteiro = (n1)
print('O valor digitado foi {} e sua parte fracionada é {}'.format(n1,trunc(n1_inteiro)))