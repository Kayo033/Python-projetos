#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Desenvolva um programa
#Que sorteie o nome de um dos alunos.

import random

a1 = str(input('Nome do primeiro aluno:'))
a2 = str(input('Nome do segundo aluno:'))
a3 = str(input('Nome do terceiro aluno:'))
a4 = str(input('Nome do quarto aluno:'))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido é o {}'.format(escolhido))

