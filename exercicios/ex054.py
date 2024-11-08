from datetime import date

menor_idade = 0
maior_idade = 0
ano_atual = date.today().year

for contador in range(1, 8):
    ano_nasc = int(input(f"Em que ano a {contador}º pessoa nasceu: "))
    if ano_atual - ano_nasc <= 18:
        menor_idade += 1
    else:
        maior_idade += 1

print(f"Temos {menor_idade} menores de idade.")
print(f"Temos {maior_idade} maiores de idade.")
