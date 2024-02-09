frase = 'Curso em video python'
frase_01 = '   Aprenda Python   '
#Abaixo FATIAMENTO de STRING
print(frase[9])
print(frase[9:14])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[0:])
print(frase[9::3])
print('_'*15)

#Abaixo ANALISE de STRING
print('O tamanho da frase é {} MICRO ESPAÇOS NA MEMORIA'.format(len(frase)))
print('Na variavel FRASE tem {} strings / letras "o"'.format(frase.count('o')))
print('Do inicio 0 até 13 tem quantas letras "o" = {}'.format(frase.count('o',0,13)))
print('Aonde será encontrado "DEO" na variavel FRASE {}'.format(frase.find('deo')))
print('Quando não é encontrado a string ele retorna o valor {}'.format(frase.find('Android')))
print('A palavra CURSO esta na variavel FRASE: {}'.format('Curso' in frase))
print('_'*15)

#Abaixo TRANSFORMAÇÃO de STRING
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase_01.strip())
print(frase_01.rstrip())
print(frase_01.lstrip())
print('_'*15)

#Abaixo DIVISÃO de STRING
print(frase.split())
print('_'*15)

#Abaixo JUNÇÃO de STRING
print('-'.join(frase))