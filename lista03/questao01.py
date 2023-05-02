gplays = ["Julio", "Anna", "Isabel", "Izaac", "Eduardo"]
print ("A lista contem os seguintes nomes:")
for nome in gplays:
    print (nome)
verificarNome = input("Qual nome voce quer verificar?")
if verificarNome in gplays:
    print (f"o nome {verificarNome} esta na lista!")
else:
    print(f"o nome {verificarNome} nao esta na lista!")
