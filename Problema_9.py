def omitir_vocales(cadena):
    resultado = ""

    for caracter in cadena:
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter
    return resultado

entrada_usuario = input("Ingrese una cadena de texto: ")
resultado_modificado = omitir_vocales(entrada_usuario)

print(f"Texto original: {entrada_usuario}")
print(f"Texto sin vocales: {resultado_modificado}")