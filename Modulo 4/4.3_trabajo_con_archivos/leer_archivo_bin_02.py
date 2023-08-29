"""
leer_archivo_bin_02.py

Método alternativo que lee un archivo en modo binario, utilizando el método read() sin 
argumentos para leer la totalidad del objeto bytes creado en memoria.
"""

from os import strerror

try:
    # Abre el archivo creado previamente en escribe_archivo_bin.py
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read())
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
