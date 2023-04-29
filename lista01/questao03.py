multaInicial, multaPorDia, diasEmAtraso, dividaTotal = float, float, int, float

multaInicial = float (input("Quanto é o valor inicial da dívida (apenas o número)? "))
multaPorDia = float (input("Quanto é o valor de multa por dia de atraso? "))
diasEmAtraso = int (input("Quantos dias está em atraso? "))

dividaTotal = multaInicial + (multaPorDia * diasEmAtraso)

print("O valor da dívida é R$ %.2f" % dividaTotal)