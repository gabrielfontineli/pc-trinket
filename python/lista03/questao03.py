def trocar_lugares(alunos): # Função que troca os alunos de lugar 
    n = len(alunos)
    pares = [i for i in range(n) if i % 2 != 0]
    meio = n // 2
    if meio % 2 != 0:
        meio -= 1

    for i in range(len(pares) // 2):
        alunos[pares[i]], alunos[pares[-i - 1]] = alunos[pares[-i - 1]], alunos[pares[i]]

    if meio in pares:
        meio_aluno = alunos[meio]
        del alunos[meio]
        alunos.insert(meio + 2, meio_aluno)

    return alunos   


n = int(input("Quantos alunos? "))
alunos = []
for i in range(n):
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)

nova_lista = trocar_lugares(alunos)

print("Nova lista:")
for aluno in nova_lista:
    print(aluno)
