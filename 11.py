import math
print("EL RANGO ES DE 1.0 -->10.0")
numero=float(input("Digite un numero flotante:"))
lista=["uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]

if numero >= 1.0 and numero <=10.0:
        numero=int(numero)
        print(lista[numero-1])


else:
    print("Error, Digite un numero flotante que se encuentre en el RANGO!")