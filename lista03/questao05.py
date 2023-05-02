meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Novembro", "Dezembro"]

entrada = int(input("Qual o número do mês?"))
entrada -= 1
if meses[entrada] in meses:
    print(f"O mês é {meses[entrada]}")
else:
    print(f"Não existe mes de número {entrada}")