#Faça um exercicio para mostrar as letras em MAIUSCULAS, MINUSCULAS, QUANTIDADE DE LETRAS E UM NOME e quantas letras
#Tem o primeiro nome de uma pessoa

nome = str(input('Digite seu nome completo:')).strip()
print('-'*15)
print('Vamos analisar seu nome...')
print('-'*15)

print('Seu nome em MAIÚSCULAS é {}'.format(nome.upper()))
print('Seu nome em MINÚSCULAS é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))

primeiro_nome = nome.split()[0]
tamanho_primeiro_nome = len(primeiro_nome)
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiro_nome, tamanho_primeiro_nome))

