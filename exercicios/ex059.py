import time

n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))

def som(n1, n2):
    return n1 + n2

def mul(n1, n2):
    return n1 * n2

while opcao != "5":
    if opcao == "1":
        print(f"A soma de {n1} + {n2} é {som(n1, n2)}")
        print("=-="*15)
        opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))
    elif opcao == "2":
        print(f"A multiplicação de {n1} X {n2} é {mul(n1, n2)}")
        print("=-="*15)
        opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))
    elif opcao == "3":
        maior = -float('inf')
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
        print(f"O maior número entre {n1} e {n2} é {maior}")
        print("=-="*15)
        opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))
    elif opcao == "4":
        print(f"Informe os valores novamente.")
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
        print("=-="*15)
        opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))
    else:
        print("Opção inválida. Tente novamente!")
        print("=-="*15)
        opcao = str(input(
'''[ 1 ] SOMAR
[ 2 ] MULTIPLICAÇÃO
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Qual a sua opção? '''))

print("Finalizando...")
time.sleep(3)
print("FIM DO PROGRAMA!")
