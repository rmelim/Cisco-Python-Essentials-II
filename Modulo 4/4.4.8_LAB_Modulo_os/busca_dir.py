"""
busca_dir.py -- Elaborado por Rui Duarte dos Santos Melim

El programa debe cumplir con los siguientes requisitos:

1.- Escribe una función o método llamado find que tome dos argumentos llamados path y dir. 
El argumento path debe aceptar una ruta relativa o absoluta a un directorio donde debe 
comenzar la búsqueda, mientras que el argumento dir debe ser el nombre de un directorio en 
el que deseas encontrar la ruta dada. Tu programa debería mostrar las rutas absolutas si 
encuentra un directorio con el nombre dado.

2.- La búsqueda en el directorio debe realizarse de forma recursiva. Esto significa que la 
búsqueda también debe incluir todos los subdirectorios en la ruta dada.

Entrada de muestra: 
path="./tree"
dir="python"

Salida de muestra:
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python

NOTA:
Existe una estructura predefinida para el ejercicio propuesto para este programa. Para poder 
cumplir a cabalidad con el mismo, se decidió crear dicha estructura en inicio del programa y
al finalizar se borra la misma.
"""

import os


def estructura(switch=True):
    if switch:
        os.makedirs("./tree/c/other_curses/cpp")
        os.mkdir("./tree/c/other_curses/python")
        os.makedirs("./tree/cpp/other_curses/c")
        os.mkdir("./tree/cpp/other_curses/python")
        os.makedirs("./tree/python/other_curses/c")
        os.mkdir("./tree/python/other_curses/cpp")
    else:
        os.removedirs("./tree/c/other_curses/cpp")
        os.removedirs("./tree/c/other_curses/python")
        os.removedirs("./tree/python/other_curses/cpp")
        os.removedirs("./tree/python/other_curses/c")
        os.removedirs("./tree/cpp/other_curses/python")
        os.removedirs("./tree/cpp/other_curses/c")


def find(path, dir):
    resp = []
    path = "./" + path if path[0:2] != "./" else path
    directorios = os.listdir(path)
    for directorio in directorios:
        if directorio == dir:
            resp.append(path + "/" + dir)
        else:
            nueva = find(path + "/" + directorio, dir)
            if len(nueva) != 0:
                resp.append(nueva.pop())
    return resp


estructura()
ruta = input("Indique ruta para iniciar la búsqueda: ")
nomb_dir = input("Indique nombre de directorio a buscar: ")
try:
    lista_dirs = find(ruta, nomb_dir)
except FileNotFoundError:
    print("Error. La ruta de inicio no existe")
else:
    if len(lista_dirs) == 0:
        print(f"El directorio {nomb_dir} no se encont´ro en ningún lado.")
    else:
        lista_dirs.sort(reverse=True)
        for d in lista_dirs:
            print(d)
finally:
    estructura(False)
