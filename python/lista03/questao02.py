N = int(input("Qual o N? "))

numeros = []

print("Digite os valores:")
for _ in range(N):
    numero = float(input())
    numeros.append(numero)

op = int(input("Qual a op? "))
A = int(input("Qual o A? "))
B = int(input("Qual o B? "))

valor_A = numeros[A-1]
valor_B = numeros[B-1]

if op == 0:
    resultado = valor_A + valor_B
    operacao = "+"
elif op == 1:
    resultado = valor_A * valor_B
    operacao = "*"
else:
    print("Operação inválida!")
    exit()

print(f"{valor_A} {operacao} {valor_B} = {resultado}")
