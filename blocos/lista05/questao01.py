def parOuImpar(valor):
    if valor % 2 == 0:
        print(f"{valor} é par")
    else:
        print(f"{valor} é ímpar")
entrada = int(input("Qual valor você quer testar? "))

parOuImpar(entrada)