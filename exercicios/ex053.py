word = input("Digite alguma palavra ou frase: ")
td_word = word.lower().replace(" ", "").replace(",", "").replace(".", "")
# td_word = MINÚSCULAS
# REPLACE(" ", "") = REMOVE OS ESPAÇOS EM BRANCO
# REPLACE(",", "") = REMOVE TODAS AS VÍRGULAS
# REPLACE(".", "") = REMOVE TODOS OS PONTOS

invert_word = td_word[::-1]

if td_word == invert_word:
    print(f"O inverso de {td_word} é {invert_word}")
    print(f"TEMOS UM PALÍNDRO!")
else:
    print(f"O inverso de {td_word} é {invert_word}")
    print(f"NÃO TEMOS UM PALÍNDRO!")
