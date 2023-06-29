quantidade_alunos = int(input("Quantos nomes? "))

nomes_alunos = []

for _ in range(quantidade_alunos):
    nome = input()
    nomes_alunos.append(nome)

print("Você digitou:")
for nome in reversed(nomes_alunos):
    print(nome)
