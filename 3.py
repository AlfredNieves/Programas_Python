palabra=str(input("Ingrese una palabra:"))
vocales=('a','e','i','o','u','A','E','I','O','U')
for vocal in vocales:
    palabra=palabra.replace(vocal, "")

print(palabra)
