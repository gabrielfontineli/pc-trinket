n1 = float(input("n1? "))
n2 = float(input("n2? "))
n3 = float(input("n3? "))

if n1 == n2 == n3:
    print("Todos são iguais a", n1)
elif n1 != n2 and n1 != n3 and n2 != n3:
    maior = max(n1, n2, n3)
    menor = min(n1, n2, n3)
    meio = n1 + n2 + n3 - maior - menor
    print("Maior:", maior)
    print("Menor:", menor)
    print("Meio:", meio)
else:
    if n1 == n2:
        maior = max(n1, n3)
        menor = min(n1, n3)
        print("Maior(es):", maior)
        print("Menor(es):", menor)
        print("Não há elementos do meio")
    elif n1 == n3:
        maior = max(n1, n2)
        menor = min(n1, n2)
        print("Maior(es):", maior)
        print("Menor(es):", menor)
        print("Não há elementos do meio")
    else:  # n2 == n3
        maior = max(n2, n1)
        menor = min(n2, n1)
        print("Maior(es):", maior)
        print("Menor(es):", menor)
        print("Não há elementos do meio")
