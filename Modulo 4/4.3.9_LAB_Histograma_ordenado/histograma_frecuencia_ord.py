"""
histograma_frecuencia_ord.py -- Elaborado por Rui Duarte dos Santos Melim

En este programa se mejora el código del LAB 4.3.8
Se hacen algunas enmiendas que generan los siguientes resultados:

1.- El histograma de salida se ordenará en función de la frecuencia de los caracteres 
(el contador más grande debe presentarse primero).
2.- El histograma debe enviarse a un archivo con el mismo nombre que el de entrada, 
pero con la extensión '.hist' (debe concatenarse con el nombre original).

Suponiendo que el archivo de prueba contiene solo una línea con: cBabAa
y se llama samplefile.txt

El resultado esperado debería verse de la siguiente manera:

a -> 3
b -> 2
c -> 1

Y el archivo resultante sería samplefile.hist

Consejo: Se puede emplear una lambda para cambiar el ordenamiento.
"""

from os import strerror

# En este caso se utiliza comprensión para crear el diccionario
letras = {chr(x): 0 for x in range(ord("a"), ord("z") + 1)}

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

try:
    filename = filename.replace(".txt", ".hist")
    hist = open(filename, "wt", encoding="utf-8")
    for key, value in sorted(letras.items(), key=lambda x: x[1], reverse=True):
        if value != 0:
            hist.write(key + " -> " + str(value) + "\n")
            print(key, "->", value)
    hist.close()
except IOError as e:
    print(f"Se produjo un error E/S al crear o escribir {filename}: ", strerror(e.errno))
