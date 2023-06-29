#dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos existem no intervalo [n1, n2], incluindo esses dois números.  
input1 = int(input("Digite o primeiro número: "))
input2 = int(input("Digite o segundo número: "))
cont = 0
for i in range(input1, input2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            cont += 1
print(f"Existem {cont} números primos no intervalo entre {input1} e {input2}")
    