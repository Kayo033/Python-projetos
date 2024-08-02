# ENTRADAS
imovel = float(input('Qual o valor do imovel? R$ '))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos será o financiamento: '))

# CALCULOS
valor_Parcelas = imovel / (anos * 12)
valorMinimo = salario * 30 / 100
# print('Parcela: {} COMP 30% do salario: {}'.format(valor_Parcelas, valorMinimo))

# CONDIÇÕES
if valorMinimo >= valor_Parcelas:
    print('Com o valor do imóvel sendo R${:.2f} e com {} anos de financiamento, as parcelas ficaram no valor de R${:.2f}'.format(imovel, anos, valor_Parcelas))
    print('EMPRESTIMO LIBERADO!')
else:
    print('Com o valor do imóvel sendo R${:.2f} e com {} anos de financiamento e parcelas de R${:.2f}'.format(imovel, anos, valor_Parcelas))
    print('EMPRESTIMO NEGADO!')
