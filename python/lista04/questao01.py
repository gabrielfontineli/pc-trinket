def criptografar(palavra):
    resultado = ''
    palavra = palavra.lower()
    
    for letra in palavra:
        if letra >= 'a' and letra <= 'e':
            resultado += '1'
        elif letra >= 'f' and letra <= 'j':
            resultado += '2'
        elif letra >= 'k' and letra <= 'o':
            resultado += '3'
        elif letra >= 'p' and letra <= 'z':
            resultado += '4'
        else:
            resultado += '5'
    return resultado

texto = input("Digite o texto: ")
encriptado = criptografar(texto)
print("Encriptado:", encriptado)
