"""
evalua_result_estudiante.py -- Elaborado por Rui Duarte dos Santos Melim

El profesor Jekyll dirige clases con estudiantes y regularmente toma notas en un archivo de texto. 
Cada línea del archivo contiene 3 elementos: el nombre del alumno, el apellido del alumno y 
el número de puntos que el alumno recibió durante ciertas clases.

Los elementos están separados con espacios en blanco. Cada estudiante puede aparecer más de una vez 
dentro del archivo del profesor Jekyll.

El archivo puede tener el siguiente aspecto:

John     Smith    5
Anna     Boleyn   4.5
John     Smith    2
Anna     Boleyn   11
Andrew   Cox      1.5

Este programa debe permitir hacer lo siguiente:

1.- Pida al usuario el nombre del archivo del profesor Jekyll.
2.- Lea el contenido del archivo y cuenta la suma de los puntos recibidos por cada estudiante.
3.- Imprima un informe simple (pero ordenado), como este:
Andrew   Cox      1.5
Anna     Boleyn   15.5
John     Smith    7.0

Nota:
el programa debe estar completamente protegido contra todas las fallas posibles: 
* la inexistencia del archivo
* El vacío del archivo
* Cualquier falla en los datos de entrada
Encontrar cualquier error de datos debería causar la terminación inmediata del programa 
y lo erróneo deberá presentarse al usuario. 

Se implementa y usa su propia jerarquía de excepciones: 
* Las excepcioens son: StudentsDataException, BadLine, FileEmpty
* la segunda excepción se debe generar cuando se detecta una línea incorrecta
* La tercera cuando el archivo fuente existe pero está vacío.

Consejo: Se pùede emplear un diccionario para almacenar los datos de los estudiantes.
"""

from os import strerror


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self, bad_line=""):
        super().__init__(self)
        self.bad_line = bad_line


class FileEmpty(StudentsDataException):
    def __init__(self, file=""):
        super().__init__(self)
        self.file = file


data_dict = {}  # Diccionario de datos vacío
try:
    filename = input("Indique nombre del archivo a procesar: ")
    # El uso de "with" aprovecha mejor la asignación de recursos al emplear excepciones.
    with open(filename, "rt", encoding="utf-8") as notas:
        if len(notas.read()) == 0:  # Lee todo el archivopara saber si está vacío.
            raise FileEmpty(filename)
        notas.seek(0)  # Reinicia el archivo desde el principio.
        for reg in notas:  # Lee cada "registro" en el archivo
            fields = reg.split()  # Divide el "registro" en sus "campos"
            if len(fields) < 3:  # Verifica que sean 3 "campos"
                raise BadLine(" ".join(fields))
            if not fields[2].replace(".", "").isnumeric():  # Verifica que el "campo" sea un número
                raise BadLine(" ".join(fields))
            key = fields[0].lower() + " " + fields[1].lower()  # Clave para el diccionario de datos
            nota = float(fields[2])  # El valor de la clave para el diccionario de datos
            if key not in data_dict:
                data_dict[key] = nota  # Crea la clave y guarda su valor
            else:
                data_dict[key] += nota  # Si ya existe, la acumula

    # Imprime el listado en forma ordenada
    for key, nota in sorted(data_dict.items(), key=lambda x: x[0]):
        print(key.split()[0].capitalize(), key.split()[1].capitalize(), nota)

# Manejo de excepciones de error
except IOError as err:
    print(f"Error de E/S al intentar abrir un archivo. Archivo inexistente. {strerror(err.errno)}")
except FileEmpty as err:
    print(f"El archivo {err.file} está vacio.")
except BadLine as err:
    print(f"Error en una línea del archivo. La linea sólo contiene: {err.bad_line}")
