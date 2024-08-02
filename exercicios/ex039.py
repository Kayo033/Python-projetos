from datetime import date
anoAtual = date.today().year #ANOATUAL recebe o ano atual da máquina

sexo = str(input('[M] Masculino \n'
                 '[F] Feminino \n'
                 'Digite seu Sexo: '))
sexoFormat = sexo.upper() #Transforma VAR SEXO em Maiuscula

if sexoFormat == "F":
    print('No Brasil, mulher não precisa se alistar!')
elif sexoFormat == "M":
    anoNasc = int(input('Ano de Nascimento: '))
    idade = anoAtual - anoNasc
    maiorIDade_alistamento = idade - 18
    menorIdade_alistamento = 18 - idade

    print(f'Quem nasceu em {anoNasc} tem {idade} anos em {anoAtual}.')

    if idade > 18:
        ano_alistamento = anoAtual - maiorIDade_alistamento
        print(f'Você já deveria ter se alistado há {maiorIDade_alistamento} anos.')
        print(f'Seu alistamento foi em {ano_alistamento}')
    elif idade < 18:
        ano_alistamento = anoAtual + menorIdade_alistamento
        print(f'Ainda faltam {menorIdade_alistamento} anos para você se alistar.')
        print(f'Seu alistamento será em {ano_alistamento} anos')
    else:
        print('Vai se alistar agora, sujeito!')
else:
    print('[ERRO], digite uma opção válida!')
