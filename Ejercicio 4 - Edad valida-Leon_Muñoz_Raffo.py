"""Ejercicio 4 - Edad valida
Pedir una edad por teclado. Antes de usarla como numero, revisar que el dato tenga sentido.

El programa tiene que aceptar edades numericas entre 0 y 120. Si la persona escribe espacios de mas, el programa deberia poder limpiarlos antes de validar.

Si el dato sirve, mostrar algo como:

Edad registrada: 25
Si no sirve, mostrar un mensaje de error claro. No alcanza con que el programa se rompa."""

edad=str(input("Edad: ")).strip()
if edad.isnumeric():
    edad_num=int(edad)
    if 0<=edad_num<=120:
        print(f"la edad fue registrada como {edad}")
    else:
        print("datos fuera de rango")
else:
    print("tipo de dato no valido")