soma_idade = 0
maior_idade_h = 0
nome_velho_h = ''
total_f = 0

for i in range(1, 5):
    print(f"-----{i}º PESSOA-----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").lower()

    soma_idade +=idade
    
    if i == 1 and sexo == 'm':
        maior_idade_h = idade
        nome_velho_h = nome
    if sexo == 'm' and idade > maior_idade_h:
        maior_idade_h = idade
        nome_velho_h = nome

    if sexo == "f" and idade < 20:
        total_f +=1

media = soma_idade / 4

print(f"A média de idade do grupo é de {media:.1f} anos.")
print(f"O homem mais velho tem {maior_idade_h} anos e se chama {nome_velho_h}.")
print(f"Ao todo são {total_f} mulher com menos de 20 anos.")
