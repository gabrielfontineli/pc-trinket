N = int(input("n? "))

if not (0 < N < 10):
    print("O número deve estar dentro do intervalo de 1 a 9.")
else:
    for i in range(1, N + 1):
        print(str(i) * i)
