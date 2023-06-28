num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

menor = min(num1,num2)
maior = max(num1, num2)

resposta = []

for i in range(menor + 1, maior):
    if i % 2 == 0:
        resposta.append(i)
for i in range(len(resposta)):
    if i != 0:
        print (",", end='')
    print (resposta[i], end='')
