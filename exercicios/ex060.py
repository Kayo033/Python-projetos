# from math import factorial

# n = int(input("Digite um número para descobrir seu fatorial: "))
# f = factorial(n)

# print(f"o fatorial de {n}! é {f}.")


# n = int(input("Digite um número para descobrir seu fatorial: "))
# c = n
# f = 1

# print(f"Calculando {n}! = ", end='')
# while c > 0:
#     print(f"{c}", end='')
#     print(f" x " if c > 1 else ' = ', end='')
#     f *= c
#     c -=1

# print(f"{f}")


n = int(input("Digite um número para descobrir seu fatorial: "))
c = 0

for c in range(n, c, -1):
    print(c, end=' ')
