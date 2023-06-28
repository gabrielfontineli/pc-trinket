meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

entrada = int(input("Qual o número do mês?"))
if entrada > 0 and entrada < 13:
    print(f"O mês é {meses[entrada-1]}")
else:
    print(f"Não existe mes de número {entrada}")