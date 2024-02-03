# #Escreva um programa que converta a temperatura de ºC para ºF

c = float(input('Digite a temperatura em C°: '))
#Na variavel F abaixo, tanto faz colocar os parenteses ou não por causa da ordem de precedência
f = (9 / 5 * c) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(c, f))