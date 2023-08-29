"""
escribe_archivo_texto_01.py -- Escribe un archivo desde cero, línea a línea
"""

from os import strerror

try:
    # Se agrega el utf-8 para que procese bien los caracteres en español
    file = open('newtext.txt', 'wt', encoding='utf-8')  # Un nuevo archivo (newtext.txt) es creado.
    for i in range(10):
        file.write("línea #" + str(i + 1) + "\n")
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
