"""
histograma_frecuencia.py -- Elaborado por Rui Duarte dos Santos Melim

Un archivo de texto contiene algo de texto (nada inusual) pero necesitamos saber con qué frecuencia
aparece cada letra en el texto. Tal análisis puede ser útil en criptografía, por lo que queremos 
poder hacerlo en referencia al alfabeto latino.

El programa tiene que:

1.- Pedir al usuario el nombre del archivo de entrada.
2.- Leer el archivo (si es posible) y cuente todas las letras latinas 
(las letras mayúsculas y minúsculas se tratan como iguales).
3.- Imprima un histograma simple en orden alfabético 
(solo se deben presentar recuentos distintos de cero).

NOTA:
Tener o crear un archivo de prueba para verifica si el histograma contiene resultados válidos.
Suponiendo que archivo de prueba contiene una sólo línea  de texto con: aBc

El resultado debería mostrarse así:

a -> 1
b -> 1
c -> 1

Consejo: Un diccionario es un medio perfecto de recopilación de datos para almacenar los recuentos.
Las letras pueden ser las claves mientras que los contadores pueden ser los valores.
"""

from os import strerror

letras = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0,
    "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "ñ": 0, "o": 0, "p": 0, "q": 0,
    "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
}

filename = input("Ingresa el nombre del archivo a analizar: ")
try:
    for line in open(filename, 'rt', encoding='utf-8'):
        for rep in [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]:
            line = line.replace(rep[0], rep[1])
        for char in line:
            if char.isalpha():
                letras[char.lower()] += 1
except IOError as e:
    print(f"Se produjo un error E/S al abrir o leer {filename}: ", strerror(e.errno))
    exit(e.errno)

for key, value in letras.items():
    if value != 0:
        print(key, "->", value)
