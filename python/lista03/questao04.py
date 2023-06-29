def calcular_percentual(total, sucesso):
    if total == 0:
        return 0
    return (sucesso / total) * 100


N = int(input("Quantidade de jogadores? "))

total_saques = 0
sucesso_saques = 0
total_bloqueios = 0
sucesso_bloqueios = 0
total_ataques = 0
sucesso_ataques = 0

print("Digite os dados para cada jogador:")

for _ in range(N):
    jogador = input().split()
    saques = int(jogador[1])
    bloqueios = int(jogador[2])
    ataques = int(jogador[3])
    sucesso_saques_jogador = int(jogador[4])
    sucesso_bloqueios_jogador = int(jogador[5])
    sucesso_ataques_jogador = int(jogador[6])

    total_saques += saques
    sucesso_saques += sucesso_saques_jogador
    total_bloqueios += bloqueios
    sucesso_bloqueios += sucesso_bloqueios_jogador
    total_ataques += ataques
    sucesso_ataques += sucesso_ataques_jogador

percentual_saques = calcular_percentual(total_saques, sucesso_saques)
percentual_bloqueios = calcular_percentual(total_bloqueios, sucesso_bloqueios)
percentual_ataques = calcular_percentual(total_ataques, sucesso_ataques)

print("As estatísticas do jogo são as seguintes:")
print(f"Pontos de Saque: {percentual_saques:.2f}%")
print(f"Pontos de Bloqueio: {percentual_bloqueios:.2f}%")
print(f"Pontos de Ataque: {percentual_ataques:.2f}%")
