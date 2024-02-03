meses = {
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}

fecha_input = input("Ingrese la fecha (en formato mes/día/año o Mes dia, año): ")
palabras = fecha_input.split()

if '/' in fecha_input:
    mes, dia, anio = fecha_input.split('/')
    mes, dia, anio = int(mes), int(dia), int(anio)
else:
    mes = meses[palabras[0]]
    dia = int(palabras[1][:-1])
    anio = int(palabras[2])

fecha_formateada = f"{anio:04d}-{mes}-{dia:02d}"
print("Fecha formateada:", fecha_formateada)