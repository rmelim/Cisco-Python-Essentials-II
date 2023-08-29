"""
leer_archivo_texto_03.py -- Lee el archivo text.txt linea por línea - método readline()
"""

from os import strerror

try:
    character_counter = line_counter = 0
    # Se agrega el utf-8 para que procese bien los caracteres en español
    stream = open('text.txt', 'rt', encoding='utf-8')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
