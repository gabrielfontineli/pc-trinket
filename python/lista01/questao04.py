textA = (input('Digite o texto A: '))
halfA = len(textA)//2
textB = (input('Digite o texto B: '))
halfB = len(textB)//2

a1 = textA[:halfA]
a2 = textA[halfA:] 

b1 = textB[:halfB]
b2 = textB[halfB:] 

print(f"Texto A dividido em duas Partes: {a1} e {a2}")
print(f"Texto B dividido em duas Partes: {b1} e {b2}")
print(f"{a1} + {b2} = {a1}{b2} ")
print(f"{a2} + {b1} = {a2}{b1} ")
print(f"{textA[0]} + {textB[1]} + {textA[-1]} + {textB[-1]}")