def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

num = int(input("Ingrese un numero: "))

if es_primo(num):
    print(f"{num} es un numero primo")
else:
    print(f"{num} no es un numero primo")