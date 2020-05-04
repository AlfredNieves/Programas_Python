cantidad=10
suma=0
numeros=[]

for i in range(0,cantidad):
    num=float(input(f"{i+1}->Ingrese  el numero:"))
    numeros.append(num)
    numeros.sort(reverse=True)
print(numeros)