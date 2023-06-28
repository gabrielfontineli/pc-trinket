valorCombustivel, valorEmReal, qtdAbastecida = float, int, float

print("Qual o valor do combustível?")
valorCombustivel = float(input())
print("Quanto você quer abastecer (apenas número)?")
valorEmReal = int(input())

qtdAbastecida = valorEmReal/valorCombustivel

print("A quantidade abastecida é %.2f Litros" % (qtdAbastecida))
