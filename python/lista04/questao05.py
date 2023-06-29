def ler_valores():
    N = int(input("N? "))
    valores = []
    print("Quais os valores?")
    for _ in range(N):
        valores.append(int(input()))
    return valores

def encontrar_par_proximo(valores):
    valores.sort()  # Ordena a lista em ordem crescente
    diferenca_minima = float("inf")  # Valor inicial da diferença mínima
    par_proximo = None

    for i in range(len(valores) - 1):
        diferenca = abs(valores[i] - valores[i + 1])
        if diferenca < diferenca_minima:
            diferenca_minima = diferenca
            par_proximo = (valores[i], valores[i + 1])

    return par_proximo

valores = ler_valores()
par_proximo = encontrar_par_proximo(valores)

print("Par mais próximo:", par_proximo[0], "e", par_proximo[1])
