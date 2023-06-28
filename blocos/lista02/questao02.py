print("Entrada: \nDigite quatro numeros:")

a = int(input())
b = int(input())
c = int(input())
d = int(input())

maior = a
menor = a

if b > maior:
    maior = b
elif c > maior:
    maior = c
elif d > maior:
    maior = d

if b < menor:
    menor = b
    if c < menor:
        menor = c
        if d < menor:
            menor = d

print("maior: " + str(maior))
print("menor: " + str(menor))
