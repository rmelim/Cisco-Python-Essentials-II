"""
lee_escribe_archivo_texto.py -- Elaborado por Rui Duarte dos Santos Melim 

Ejemplo en donde se lee un archivo y se escribe lo leído hacia un nuevo archivo.
"""

from os import strerror

try:
    lcnt = 0
    # Se agrega el utf-8 para que procese bien los caracteres en español
    new_file = open('poema.txt', 'wt', encoding='utf-8')  # Un nuevo archivo (poema.txt) es creado.
    # Lee el archivo de forma iterable. Al finalizar la iteración, el mismo objeto cierra el archivo
    for line in open('text.txt', 'rt', encoding='utf-8'):
        lcnt += 1
        new_file.write(line)  # Escribimos la línea leída al nuevo archivo
    new_file.close()
    print("Líneas leídas y transferidas en el archivo:", lcnt)

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
