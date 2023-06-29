# Lê os três textos do usuário
texto1 = input("Texto 1? ").lower()
texto2 = input("Texto 2? ").lower()
texto3 = input("Texto 3? ").lower()

# Cria uma lista com os textos
textos = [texto1, texto2, texto3]

# Ordena os textos em ordem lexicográfica
textos.sort()

# Imprime os textos em ordem
print("Seguem os textos em ordem:")
for i, texto in enumerate(textos, start=1):
    print(f"{i}o. {texto}")
