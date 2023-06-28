salario = int(input("Qual o valor do seu salário? "))
despesa = int(input("Qual sua despesa mensal? "))
acumuloAnual = (salario - despesa) * 12

tempoTotal = 1000000/acumuloAnual 
meses = float (tempoTotal % 1)
print(f"Você vai demorar {int(tempoTotal)} anos e {round(meses*12)} meses para poupar milhão")
