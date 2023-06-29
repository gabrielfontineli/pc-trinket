def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n1 = int(input("Digite o número n1: "))
n2 = int(input("Digite o número n2: "))

if n1 > n2:
    n1, n2 = n2, n1

print("Números ímpares não primos entre[", n1, "-", n2, "] :", end=' ')

for num in range(n1, n2 + 1):
    if num % 2 != 0 and not is_primo(num):
        print(num, end=' ')
