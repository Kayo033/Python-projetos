num = int(input('Digite um numero inteiro: '))
print('Escolha umas das bases para conversão:')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opt = int(input('Sua opção: '))

if (opt == 1):
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:])) # [2:] escreve somente a partir da 3 palavra
elif (opt == 2):
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:])) # [2:] escreve somente a partir da 3 palavra
elif (opt == 3):
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:])) # [2:] escreve somente a partir da 3 palavra
else:
    print('Opção invalida, tente novamente!')
