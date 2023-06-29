def obter_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

N = int(input("Qual o valor de N? "))
print("Digite os valores:")
numeros = []
for _ in range(N):
    numeros.append(int(input()))

print("A classificação é:")
for numero in numeros:
    divisores = obter_divisores(numero)
    if len(divisores) == 2:
        print(numero, "é primo")
    else:
        print(numero, "não é primo, os divisores são:", divisores)
