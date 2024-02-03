numeros_divisibles = []

for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_divisibles.append(numero)

print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(numeros_divisibles)