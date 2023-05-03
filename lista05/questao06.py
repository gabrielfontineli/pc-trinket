def idadeEmDias(a,m,d):
    return (a * 365 + m * 30 + d)

print("Informe a idade da pessoa em anos, meses e dias")

anos = int(input("anos: "))
meses = int(input("meses: "))
dias = int(input("dias: "))

print(f"A pessoa já viveu {idadeEmDias(anos,meses,dias)} dias")