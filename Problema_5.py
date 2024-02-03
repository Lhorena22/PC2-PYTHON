def contar(numero, digito):
    cadena = str(numero)
    cantidad = cadena.count(str(digito))
    return cantidad

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese el digito que desea verificar: "))

cantidad = contar(numero, digito)

print(f"Número ingresado: {numero} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {cantidad}")