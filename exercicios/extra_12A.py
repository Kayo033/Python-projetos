prod = float(input('Digite o valor do produto R$'))
des = float(input('Digite a porcentagem de desconto %'))

final = prod - (prod * des / 100)

print('O valor de desconto foi R${} e o preço final é R${}'.format(des,final))