"""
leer_archivo_texto_02.py -- Lee el archivo text.txt por completo
"""

from os import strerror

try:
    counter = 0
    # Se agrega el utf-8 para que procese bien los caracteres en español
    stream = open("text.txt", "rt", encoding='utf-8')
    content = stream.read()
    for char in content:
        print(char, end='')
        counter += 1
    stream.close()
    print("\n\nCaracteres en el archivo:", counter)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
