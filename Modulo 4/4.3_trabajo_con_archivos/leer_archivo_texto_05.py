"""
leer_archivo_texto_05.py -- Lee el archivo text.txt como un objeto iterable
"""

from os import strerror

try:
    ccnt = lcnt = 0
    # Lee el archivo de forma iterable. Al finalizar la iteración, el mismo objeto cierra el archivo
    for line in open('text.txt', 'rt', encoding='utf-8'):
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en el archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
