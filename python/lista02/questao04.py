n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))

if not (1 <= n1 <= n2 <= 10):
    print("Os números devem estar dentro do intervalo de 1 a 10.")
else:
    for num in range(n1, n2 + 1):
        print("=-=-=-=- Tabuada de", num, "-=-=-=-=")
        for i in range(1, 11):
            resultado = num * i
            print(num, "x", i, "=", resultado)
