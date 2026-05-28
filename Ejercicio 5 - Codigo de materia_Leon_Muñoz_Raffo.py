"""Ejercicio 5 - Codigo de materia
Pedir al usuario un codigo de materia con este formato:

PROG-101
El programa tiene que validar que:

tenga un solo guion -;
la parte de la izquierda tenga solo letras;
la parte de la derecha tenga solo numeros.
Si el codigo es valido, mostrarlo normalizado en mayusculas (metodo upper).

Ejemplo:

Codigo valido: PROG-101
Si no es valido, mostrar un mensaje de error claro."""

codigo=str(input("dame el codigo: "))
if codigo.count("-")==1:
    codigo1=codigo.strip(" ").split("-")
    if codigo1[1].isnumeric():
        if codigo1[0].isalpha():
            print (f"codigo valido:{codigo.upper()}")
        else:
            print(f"codigo {codigo} no valido")
    else:
        print(f"codigo {codigo} no valido")
else:
    print(f"codigo {codigo} no valido")
