#Faça um programa que leia os Catetos Oposto e Adjacente e mostre o comprimento da Hipotenusa

#import math = Com somente IMPORT MATH tenho que colocar o MATH.SQRT na variavel hipotenusa
from math import sqrt

oposto = float(input('Comprimento do Cateto Oposto:'))
adjacente = float(input('Comprimento do Cateto Adjacente:'))

x = oposto * oposto + adjacente * adjacente
# Usando a função SQRT() para calcular a raiz quadrada
hipotenusa = sqrt(x)

print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))


# Usando a função hypot() para calcular a hipotenusa
# hipotenusa = math.hypot(3, 4)
# print(hipotenusa)
