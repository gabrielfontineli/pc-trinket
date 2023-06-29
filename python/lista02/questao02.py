#generate N first numbers of fibonacci sequence 
def fibonacci(n):    
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
entry = int(input("Digite o número de termos: "))
print("Sequência de Fibonacci: ")
for i in range(entry):  
    print(fibonacci(i), end=' ')