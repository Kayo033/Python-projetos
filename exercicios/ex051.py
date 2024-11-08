print("→→"*20)
print("         10 TERMOS DE UMA PA          ")
print("→→"*20)

termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

# RANGE(10), Garante a reprodução do loop 10X
for i in range(10):
    print(f"{termo}", end=" ")
    # A cada loop, o TERMO recebe ele mais a RAZAO
    termo += razao
print("FIM!")
