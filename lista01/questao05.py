salarioAtual = float(input("Qual o salário atual? "))
ajustePercentual = float(input("Qual o percentual de ajuste? "))

reajuste = salarioAtual * (ajustePercentual/100)
salarioFinal = reajuste + salarioAtual

print(f"o reajuste foi de {int(reajuste)} reais e {int(reajuste % 1 *100)} centavos" )
print(f"o reajuste foi de {int(salarioFinal)} reais e {int(salarioFinal % 1 *100)} centavos" )