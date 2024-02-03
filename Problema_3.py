pares = 0
impares = 0

while True:
    opcion = input("¿Desea ingresar un número? (s/n): ").lower()
    if opcion != 's':
        break
    entrada = input("Ingrese un número: ")
    if entrada.isdigit():
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        print("Error: Por favor, ingrese un número válido.")

print(f"\nCantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
