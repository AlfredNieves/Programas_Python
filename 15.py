cantidad=10
numeros=[]
primos=[]
print("DIGITE 10 NUMEROS!")
for i in range(0,cantidad):
    num=int(input(f"Ingrese el numero:"))
    numeros.append(num)
    if num > 1:
        cont=0
        i=2
        while i<num and cont==0:
            residuo=num%i
            if residuo==0:
                cont+=1
            i+=1
        if cont==0:
            primos.append(num)
print(f"Numeros primos ingresados:{primos}")