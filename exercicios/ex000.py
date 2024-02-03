print('Seja bem-vindo ao calculo de IMC(INDICE DE MASSA CORPORAL)')

nome = input('Qual é o seu nome:')
peso = float(input('Qual é o seu peso:'))
altura = float(input('Qual é a sua altura:'))

print('Vamos descobrir seu IMC')

imc = peso / (altura * altura)

print('Nome:', nome, '\nPeso:', peso, '\nAltura:', altura)
print(f'Seu IMC é: {imc:.2f}')

# fazer IF, ELIF, ELSE

if imc < 17:
    print('Magreza Grave!')
elif 17 <= imc < 18.5:
    print('Magreza Leve!')
elif 18.5 <= imc < 24.9:
    print('Eutrófico!')
elif 25 <= imc < 29.9:
    print('Sobrepeso!')
elif 30 <= imc < 34.9:
    print('Obesidade I!')
elif 35 <= imc < 39.9:
    print('Obesidade Severa!')
else:
    print('Obesidade Mórbida!')
