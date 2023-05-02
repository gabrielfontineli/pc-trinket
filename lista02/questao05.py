saldo = 1000.00
while True:
    print("Escolha uma das opções:\n1 SAQUE\n2 DEPOSITO\n3 SALDO")
    entry = int(input())
    # SAQUE
    if entry == 1:
        saque = float(input("Qual valor deseja sacar?"))
        if saque <= saldo:
            saldo -= saque
            print("saque de " + str(saque) +
                  " autorizado,\nRestam " + str(saldo))
        else:
            print("saldo insuficiente")
    # DEPOSITO
    if entry == 2:
        deposito = float(input("Qual valor deseja depositar?"))
        if deposito < 0:
            print("Valor invalido")
        else:
            saldo += deposito
            print("deposito de " + str(deposito) +
                  " autorizado,\nSaldo atual de" + str(saldo))
    # SALDO
    if entry == 3:
        print("Saldo atual eh de " + str(saldo))
