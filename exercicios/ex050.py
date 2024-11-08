c = 0
s = 0

for i in range (1,7):
    i = int(input(f"Digite {i}º valor: "))
    if i % 2 == 0:
        s +=i
        c +=1

print(f"A soma dos {c} números pares informados é {s}")
