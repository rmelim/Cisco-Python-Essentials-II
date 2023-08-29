"""
escribe_archivo_bin_01.py -- Escribe un archivo en modo binario (bytearray)
"""

from os import strerror

data = bytearray(10)  # Crea un objeto bytearray de 10 bytes

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')  # Crea el archivo file.bin en modo escritura
    bf.write(data)
    bf.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
