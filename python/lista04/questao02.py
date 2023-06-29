def exibeOpcoes():
    print('Qual operação você deseja realizar?')
    print('1 - SAQUE')
    print('2 - DEPÓSITO')
    print('3 - SALDO')
    print('4 - SAIR')
    opcao = int(input('Escolha: '))
    return opcao

def processaOpcoes(opcao, saldo):
    if opcao == 1:  # Funcionalidade de saque
        saldo = saque(saldo)
        print('Agora o seu saldo atual é de: ' + str(saldo))
    elif opcao == 2:  # Funcionalidade de depósito
        saldo = deposito(saldo)
        print('O seu saldo agora é de: ' + str(saldo))
    elif opcao == 3:  # Funcionalidade de saldo
        print('O seu saldo atual é de: ' + str(saldo))
    elif opcao == 4:  # Sair
        print('Obrigado por usar os serviços do Caixa Eletrônico')
    else:
        print('Opção inválida, tente novamente!')
    return saldo

def exibeSaldo(saldo):
    print('O seu saldo atual é de: ' + str(saldo))

def saque(saldo):
    valor_sacado = float(input('Qual valor você deseja sacar? '))
    if valor_sacado <= saldo:
        saldo -= valor_sacado
        print('Saque autorizado.')
    else:
        print('Saldo insuficiente.')
    return saldo

def deposito(saldo):
    valor_deposito = float(input('Qual o valor que você quer depositar? '))
    if valor_deposito > 0:
        saldo += valor_deposito
        print('Depósito realizado.')
    else:
        print('Valor inválido.')
    return saldo

def principal():
    saldo = 1000
    while True:
        opcao = exibeOpcoes()
        saldo = processaOpcoes(opcao, saldo)
        if opcao == 4:  # Verifica se o usuário escolheu sair
            break

principal()
