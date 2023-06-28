while True:
    gplays = int(input("Digite um numero: "))
    if gplays < 1:
        print("O numero tem que ser maior que 0")
    else:
        break

fatorial = 1

for i in range(1, gplays+1):
    fatorial = fatorial * i
print(f"Resultado fatorial: {fatorial}")
