"""
leer_archivo_texto_01.py -- Lee el archivo text.txt caracter por caracter
"""

from os import strerror

try:
    counter = 0
    # Se agrega el utf-8 para que procese bien los caracteres en español
    stream = open("text.txt", "rt", encoding='utf-8')
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
