nome = str(input('Qual é o seu nome: ')).strip() #.STRIP() remove espaços no começo e fim

if nome == 'Kayo':
    print('Que nome bonito você tem hein, {}!'.format(nome))
elif nome == 'Jesus' or nome == 'Deus':
    print('Este nome {}, é sobre todos os nomes!!!'.format(nome))
elif nome == 'Pedro' or nome == 'Tiago' or nome == 'João':
    print('Seu nome tem na Biblia, {}.'.format(nome))
elif nome == 'Maracuja' or nome == 'Goiaba':
    print('Suco de {} é muito bom!'.format(nome))
elif nome in 'Cristina Jucileudo Sofia Thor':
    print('Esse nome {}, é conhecido!'.format(nome))
else:
    print('Você tem um nome legal {}, parabéns!'.format(nome))
