usuario = input("Digite o usuário ")
while True:
    senha = input("Digite a senha: ")
    if senha == usuario:
        print("Saída: A senha nao pode ser igual ao nome do usuário")
    else:
        print("Saída: Senha válida")
        break