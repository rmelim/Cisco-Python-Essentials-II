"""
leer_archivo_bin_01.py -- lee un archivo en modo binario (bytearray) utilizando readinto()
"""

from os import strerror

data = bytearray(10)

try:
    # Abre el archivo creado previamente en escribe_archivo_bin.py
    binary_file = open('file.bin', 'rb')
    # readinto() llena el objeto bytearray con los valors tomados desde el archivo
    binary_file.readinto(data)
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
