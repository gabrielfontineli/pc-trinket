kmInicial, kmFinal, litrosConsumidos, consumoMedio = int, int, float, float

kmInicial = int (input("Qual o valor da kilometragem inicial? "))
kmFinal = int (input("Qual o valor da kilometragem final? "))
litrosConsumidos = float (input("Quantos litros foram consumidos na viagem? "))

consumoMedio = (kmFinal - kmInicial)/litrosConsumidos
print ("O valor de consumo médio é de: %.1f Km/L" % (consumoMedio))
