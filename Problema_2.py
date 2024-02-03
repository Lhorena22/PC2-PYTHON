n_asteriscos = int(input('Ingrese el numero maximo de asteriscos: '))

for i in range(1,n_asteriscos+1):
    print("* "*i)
for i in range(1,n_asteriscos+1):
    print("* "*(n_asteriscos-i))