gplays = ["Júpiter", "Saturno", "Urano", "Netuno", "Plutão"]
print("Os nomes da lista são:")
for planeta in gplays:
    print(planeta)

apagarPlaneta = input("Qual nome deseja apagar?")
if apagarPlaneta in gplays:
    gplays.remove(apagarPlaneta)
else:
    print(f"{apagarPlaneta} não foi encontrado na lista!")

print("A lista atual é:")
for planeta in gplays:
    print(planeta)
