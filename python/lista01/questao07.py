num_dias = int(input("Digite o número de dias: "))

semanas = num_dias // 7
dias_resto = num_dias % 7

mensagem_semanas = f"{semanas} semana" if semanas == 1 else f"{semanas} semanas"
mensagem_dias = f"{dias_resto} dia" if dias_resto == 1 else f"{dias_resto} dias"

if semanas == 0 and dias_resto == 0:
    print(f"{num_dias} dias equivale a nenhum dia.")
elif semanas == 0:
    print(f"{num_dias} dias equivalem a {mensagem_dias}!")
elif dias_resto == 0:
    print(f"{num_dias} dias equivalem a {mensagem_semanas}!")
else:
    print(f"{num_dias} dias equivalem a {mensagem_semanas} e {mensagem_dias}!")
