#Crie um programa que diga aonde esta a primeira e última ocorrência de uma string

frase = str(input('Digite uma frase:')).strip().upper()
print('A letra "O" apareceu {} vezes na frase'.format(frase.count('O')))
print('A primeira letra "O" apareceu na posição {}'.format(frase.find('O')))
print('A última letra "O" apareceu na posição {}'.format(frase.rfind('O')))
'''Acima no RFIND('O') o R antes de FIND, indica que sera chamada 
a ultima ocorrência da letra 'O' em FRASE'''
print('O tamanho da frase é {} espaços na memoria'.format(len(frase)))
