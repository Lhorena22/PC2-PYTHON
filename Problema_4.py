alumnos = []
numero = int(input("Ingrese el numero de alumnos: "))

for _ in range(numero):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = []

    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i+1} para {nombre}: "))
        notas.append(calificacion)

    alumno = {"Alumno": nombre, 
              "Notas": notas}
    alumnos.append(alumno)
print("""
Lista de alumnos:""")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']},\nNotas: {alumno['Notas']}\n")
