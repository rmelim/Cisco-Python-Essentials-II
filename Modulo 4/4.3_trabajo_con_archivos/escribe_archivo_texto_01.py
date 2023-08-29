"""
escribe_archivo_texto_01.py -- Escribe un archivo desde cero, caracter por caracter 
"""

from os import strerror

try:
    # Se agrega el utf-8 para que procese bien los caracteres en español
    file = open('newtext.txt', 'wt', encoding='utf-8')  # Un nuevo archivo (newtext.txt) es creado.
    for i in range(10):
        s = "línea #" + str(i + 1) + "\n"
        for char in s:
            file.write(char)
    file.close()
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
