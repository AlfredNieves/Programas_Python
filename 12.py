horas=float(input("Ingrese el número de Horas:"))
tarifa=float(input("Ingrese la tarifa:"))
dias=int(input("Digite el número de días:"))
if horas%dias==8:
    ganancia=horas*tarifa*dias
    print(f"El TOTAL de dinero GANADO es de:{ganancia}")
else:
    print("Baia Baia, alguien no trabajo jornadas completas -_-")
    print("EL NUMERO DE HORAS ACUMULADAS, NO COINCIDE CON LAS JORNADAS LABORALES TRABAJADAS")

