textA = (input('Digite o texto A: '))
textB = (input('Digite o texto B: '))
print('tamanho(A) - tamanho(B) = ' + str(len(textA) - len(textB)))
print('A + B = ' + textA+textB)
print('A contém B = ' + str(textB in textA))
print('B contém A = ' + str(textA in textB))
print('Primeira letra de A = ' + textA[0])
print('Primeira letra de B = ' + textB[0])
print('Última letra de A = ' + textA[int(len(textA) - 1)])
print('Última letra de B = ' + textB[int(len(textB) - 1)])
