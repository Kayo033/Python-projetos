preco = float(input('Digite o valor das compras: '))

# CALCULOS
opt_1 = preco - (10/100*preco)
opt_2 = preco - (5/100*preco)
opt_3 = preco
opt_4 = preco + (20/100*preco)

print('''Suas opções de pagamento:
[ 1 ] À vista dinheiro/cheque (10% de desconto)
[ 2 ] À vista cartão débito (5% de desconto)
[ 3 ] Até 2x no cartão de crédito
[ 4 ] Até 3x ou mais no cartão de crédito (20% de juros)''')
opcao = int(input('Sua escolha: '))

if opcao == 1:
    print('Valor final: R${:.2f}'.format(opt_1))
elif opcao == 2:
    print('Valor final: R${:.2f}'.format(opt_2))
elif opcao == 3:
    quant_parc = int(input('Quantas vezes será parcelado: '))
    valor_parc = preco / quant_parc
    print('A mercadoria sendo parcelada em {} vezes as parcelas serão de {}'.format(quant_parc, valor_parc))
    print('Valor final: R$ {:.2f}'.format(opt_3))
elif opcao == 4:
    quant_parc = int(input('Quantas vezes será parcelado: '))
    valor_parc = preco / quant_parc
    print('A mercadoria sendo parcelada em {} vezes com parcelas de {}'.format(quant_parc, valor_parc))
    print('O valor final será de R$ {:.2f}'.format(opt_4))
else:
    print('[ERRO] Digite uma opção válida!')
