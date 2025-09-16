print()
print("bienvenido al creador de archivos innecesarios")

Texto = input("Ingrese lo que quiere colocar en el archivo")

with open ('archivo.txt', 'w') as f:
    f.write(Texto)
    
print("hemos creado el archivo con el texto que usted nos dio, vaya que somos buenos mi loco")

print("le mostramos mire:")

with open ('archivo.txt', 'r') as f:
    contenido = f.read()
    print(contenido)

choise = input("quiere cambiar algo?: ")


if choise == 1:

    with open("archivo.txt", 'a') as f:
        f.write('\nNueva Linea')