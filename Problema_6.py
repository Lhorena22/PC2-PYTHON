def hallar_fibonacci(n):
    resultado = []
    a = 0
    b = 1
    while a <= n:
        resultado.append(a)
        a, b = b, a + b
    return resultado

print("Serie fibonacci entre el numero 0 y 50:")
print(hallar_fibonacci(50))