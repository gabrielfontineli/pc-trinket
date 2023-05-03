while True:
    gplays = int(input("Digite um numero: "))
    if gplays > 1 and gplays > 9:
        print("O numero precisa ser entre 1 e 9")
    else:
        break
for i in range(1,10):
    print(f"{gplays}x{i} = {gplays*i}")
