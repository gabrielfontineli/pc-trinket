n = int(input("Digite um número inteiro positivo: "))
i = 1
e_triangular = False

while i * (i + 1) * (i + 2) <= n:
    if i * (i + 1) * (i + 2) == n:
        e_triangular = True
        break
    i += 1

if e_triangular:
    print(n, "é triangular")
else:
    print(n, "não é triangular")
