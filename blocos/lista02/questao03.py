salario = int(input("Qual seu salario: "))
financiamento = int(input("Qual seu financiamento: "))

print("Resposta:")
if salario * 5 >= financiamento:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
print("Obrigado por nos consultar")
