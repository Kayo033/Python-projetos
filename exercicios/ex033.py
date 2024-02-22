#Faça um programa que leia três valores e mostre o maior e o menor valor
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

#Testando menor valor
menorValor = valor1
if valor2<valor1 and valor2<valor3:
    menorValor = valor2
if valor1 > valor3 and valor3<valor2:
    menorValor = valor3

#Testando maior valor
maiorValor = valor1
if valor2 > valor1 and valor2 > valor3:
    maiorValor = valor2
if valor3 > valor1 and valor3 > valor2:
    maiorValor = valor3

print('O MENOR valor foi {}.'.format(menorValor))
print('O MAIOR valor foi {}.'.format(maiorValor))
