n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7.0:
    print(f'O aluno com as notas {n1}, {n2} e {n3} está com MÉDIA {media:.2}, APROVADO!')
elif media >= 5.0 and media <= 6.9:
    print(f'O aluno com as notas {n1}, {n2} e {n3} está com MÉDIA {media:.2}, em RECUPERAÇÃO!')
else:
    print(f'O aluno com as notas {n1}, {n2} e {n3} está com MÉDIA {media:.2}, REPROVADO!')
