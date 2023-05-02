compra = float(input("Valor de compra: "))
opcaoDePgto = input("Opcao de pagamento: ")

if(opcaoDePgto.lower() == "v"):
    print("Saida: Valor a ser pago = " + str(compra))
else:
    compra *= 1.08 #compra = compra * (8/100) + compra
    print(f"Saida: Valor a ser pago = {compra} em 3 parcelas de {compra/3}")
