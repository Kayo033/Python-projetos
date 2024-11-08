import random
cont = 0

print("Eu sou seu computador...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
num_aletorio = random.randint(0, 10)
print(num_aletorio)
num_usuario = int(input("Qual é o seu palpite? "))


if num_usuario == num_aletorio:
    print(f"Parabéns, você acertou o número aleatório era {num_aletorio}.")
    print("Acertou de primeira!")
else:
    while num_usuario != num_aletorio:
        cont +=1
        if num_usuario > num_aletorio:
            print("Menos... tente novamente.")
            num_usuario = int(input("Qual é o seu palpite? "))
        elif num_usuario < num_aletorio:
            print("Mais... tente novamente.")
            num_usuario = int(input("Qual é o seu palpite? "))
    print(f"Parabéns, você acertou o número aleatório era {num_aletorio}.")
    print(f"Você precisou de {cont} tentativas para acertar.")
