# Faça um programa que leia  a largura de um parede e a altura  de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

lar= float(input('Largura da Parede: '))
alt= float(input('Altura da Parede: '))
area= lar * alt

print('Sua área é de {}m²'.format(area))

tinta= area / 2

print('Para pintar essa parece você precisará de {}L de tinta.'.format(tinta))
