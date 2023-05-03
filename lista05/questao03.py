def calcularMA(a, b, c):
    media = (a + b + c)/3
    return (media)


def calcularMP(a, b, c):
    media = (a * 5 + b * 3 + c * 2)/10
    return (media)


print("Quais são as notas?")
a = int(input())
b = int(input())
c = int(input())

tipoMedia = input("Que tipo de média você quer? ")
if tipoMedia == "A":
    print(f"A média é {calcularMA(a,b,c)}")
elif tipoMedia == "P":
    print(f"A média é {calcularMP(a,b,c)}")
