def factorial(numero):
    if numero < 0:
        return "Error: Ingrese un número no negativo."
    if numero == 0:
        return 1
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es: {resultado_factorial}")