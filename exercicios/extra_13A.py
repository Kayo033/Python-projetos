preco_1 = float(input('Digite o valor do produto R$'))
# desconto = preco_1 * (preco_1 - 10 / 100)
# aumento = preco_1 + (preco_1 + 8 / 100)

desconto = preco_1 - (preco_1 * 10 / 100)
aumento = preco_1 + (preco_1 * 8 / 100)

print('Os preços ficaram conforme abaixo \n À vista com 10% de desconto sai por R${:.2f}\n '
      'Parcelado terá um aumento de 8% saindo por R${:.2f}'.format(desconto, aumento))


