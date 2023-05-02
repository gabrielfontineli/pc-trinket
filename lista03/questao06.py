gplays = [3, 5, 4, 4, 4, 3, 2, 5, 3, 4]
print("A lista é:")
for n in gplays:
    print(n)
print("Após encontrar os números 5 a lista ficou:")
testador = 5
for indice in range(len(gplays)):
    if 5 == gplays[indice]:
        gplays[indice] = "Cinco"
for n in gplays:
    print(n)
