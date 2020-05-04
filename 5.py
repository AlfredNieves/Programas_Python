cantidad=int(input("Cuantos numeros desea ingresar:"))
suma=0
numeros=[]

for i in range(0,cantidad):
    num=float(input(f"Ingrese el numero:"))
    numeros.append(num)
    suma+=num
media=suma/cantidad
print(f"La Media Aritmética es:{media}")
from statistics import mode
from statistics import stdev
from statistics import median
print("La Moda es:",mode(numeros))
print("La Media es:",median(numeros))
print("La Desviación estandar es:",stdev(numeros))
