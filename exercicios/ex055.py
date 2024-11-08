lista_peso = [] # INICIALIZA A LISTA

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}º pessoa: "))
    lista_peso += [peso]

print(f"O maior peso lido foi {max(lista_peso)}Kg")
print(f"O menor peso lido foi {min(lista_peso)}Kg")
