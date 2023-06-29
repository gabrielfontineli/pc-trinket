def imprimePartes(lista, separador):
    print("Sequencias resultantes:")
    partes = []
    sublista = []
    
    for elemento in lista:
        if elemento == separador:
            if sublista:  # Verifica se a sublista não está vazia
                partes.append(sublista)
                sublista = []
        else:
            sublista.append(elemento)
    
    if sublista:  # Adiciona a última sublista se não estiver vazia
        partes.append(sublista)
    if partes:        
        for parte in partes:
            print(parte)
    else:
        print("Nenhuma")

N = int(input("Digite o valor de N: "))
sequencia = []
for _ in range(N):
    sequencia.append(int(input("Digite um valor da sequência: ")))

separador = int(input("Digite o valor do separador: "))

imprimePartes(sequencia, separador)
