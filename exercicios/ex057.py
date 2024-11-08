# sexo = str(input("Digite seu sexo: [M / F] ")).upper().strip()[0] 
# UPPER() = MAIUSCULA
# STRIP() = REMOVE ESPAÇOS EM BRANCO
# [0] = CAPTURA O 1º DADO DIGITADO


# while sexo not in "MF":
#     sexo = str(input("Dados invalidos. Por favor, digite seu sexo: [M/F] ")).upper().strip()[0] 

# print(f"Sexo {sexo}, foi validado com sucesso!")


sexo = str(input("Digite seu sexo: [M / F] ")).upper()

while sexo != "M" and sexo != "F":
    sexo = str(input("Dados invalidos. Por favor, digite seu sexo: [M / F] ")).upper()

print(f"Sexo: {sexo}")
print("FIM")
