def definirTriangulo(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 0
    elif (a == b) and (a == c):
        return 1
    elif (a == b) or (a == c) or (b == c):
        return 2
    else:
        return 3


print("Informe os lados")

a = int(input())
b = int(input())
c = int(input())

if definirTriangulo(a, b, c) == 0:
    print(f"Os lados [{a}, {b}, {c}] não representam um triângulo")
elif definirTriangulo(a, b, c) == 1:
    print(f"Os lados [{a}, {b}, {c}] representam um triangulo equilátero")
elif definirTriangulo(a, b, c) == 2:
    print(f"Os lados [{a}, {b}, {c}] representam um triângulo isósceles")
elif definirTriangulo(a, b, c) == 3:
    print(f"Os lados [{a}, {b}, {c}] representam um triangulo escaleno")
