"""Ejercicio 3 - Acomodar nombres
Partiendo de esta lista:

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
Armar una nueva lista llamada nombres_normalizados donde cada nombre quede sin espacios sobrantes y con un formato prolijo.

Al final, mostrar la lista. Deberia quedar parecido a esto:

["Mara", "Tomas", "Lucia", "Marcos", "Sofia"]"""

nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados=[]
for i in range (0,len(nombres)):
    nombres_normalizados.append(nombres[i].strip().capitalize())
print (nombres_normalizados)
