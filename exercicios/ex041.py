from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Ano do seu Nascimento: '))
idade = anoAtual - anoNasc

if idade < 9:
    print(f'Com {idade} anos, a categoria é MIRIM!')
elif idade < 14:
    print(f'Com {idade} anos, a categoria é INFANTIL!')
elif idade < 19:
    print(f'Com {idade} anos, a categoria é JUNIOR!')
elif idade < 25:
    print(f'Com {idade} anos, a categoria é SÊNIOR!')
else:
    print(f'Com {idade} anos, a categoria é MASTER!')
