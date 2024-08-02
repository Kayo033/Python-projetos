peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print('{:.2f} MAGREZA!'.format(imc))
elif imc > 18.5 and imc <= 24.9:
    print('{:.2f} NORMAL!'.format(imc))
elif imc > 25.0 and imc <= 29.9:
    print('{:.2f} SOBREPESO!'.format(imc))
elif imc > 30.0 and imc <= 39.9:
    print('{:.2f} OBESIDADE!'.format(imc))
elif imc > 40:
    print('{:.2f} OBESIDADE GRAVE!'.format(imc))
else:
    print('Você está tão gordo, que não tem nem classificação.')
