def fatorial(valor):
    factorial = 1
    for i in range(1,valor + 1):    
       factorial = factorial*i
    print(f"{valor}! é {factorial}")
gplays = int(input("Qual numero você gostaria de saber o fatorial? "))

fatorial(gplays)
