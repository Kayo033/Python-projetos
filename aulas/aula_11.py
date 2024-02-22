print('\033[1;35;40m Hello, world !')
print('\033[m')
print('\033[1;35;40m Hello, world !\033[m')

print('')
print('\033[7;97m Teste \033[m')

print('')
a = 'AZUL'
v = 'VERMELHO'
print('As cores serão impressas da seguinte forma \033[34m{}\033[m e \033[31m{}\033[m respectivamente.'.format(a, v))

print('')
nome = 'Kayo'
print('{}{}{}, Persista, sempre treine e nunca {}desista{} !'.format('\033[7:97m',nome,'\033[m','\033[32m','\033[m'))

print('')
nome = 'Kayo'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoeBranco':'\033[7:97m'}
print('Muito prazer em te conhecer, {}{}{}'.format(cores['pretoeBranco'], nome,cores['limpa']))
