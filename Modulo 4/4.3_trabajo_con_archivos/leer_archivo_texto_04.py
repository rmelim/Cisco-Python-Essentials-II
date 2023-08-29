"""
leer_archivo_texto_04.py -- Lee el archivo text.txt hacia una lista - método readlines()
"""

from os import strerror

try:
    ccnt = lcnt = 0
    # Se agrega el utf-8 para que procese bien los caracteres en español
    s = open('text.txt', 'rt', encoding='utf-8')
    # readlines() devuelvce la lista. Si se indica argumento, lee esa cantidad de caracteres
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCaracteres en el archivo:", ccnt)
    print("Líneas en archivo:     ", lcnt)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
