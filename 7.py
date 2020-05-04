
palabra=input("Digite la palabra:")
nombre=input("Digite el nombre del Archivo:")

file=open(f"{nombre}.txt", "a+")
file.write(palabra)
file.close()

