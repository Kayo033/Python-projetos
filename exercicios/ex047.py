n = int(input("Digite algum número: "))

# Se n for ímpar, decrementamos 1 para torná-lo par
if n % 2 != 0:
    n -= 1

for c in range(n, -1, -2):
    print(f"{c}", end=" ")

print("Acabou!")
