'''
procesador_numeros.py

Este programa muestra un método simple que permite ingresar una línea llena de números y 
sumarlos fácilmente. Nota: la función input(), combinada junto con las funciones int() o float(), 
no es lo adecuado para este propósito.

El procesamiento será extremadamente fácil: queremos que se sumen los números.

Observa el código en el editor. Analicémoslo.

Opcional:
El emplear listas por comprensión puede hacer que el código sea más pequeño. 
'''

# pide al usuario que ingrese una línea llena de cualquier cantidad de números
# (los números pueden ser flotantes).
line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()  # divide la línea en una lista con subcadenas.
total = 0  # se inicializa la suma total a cero.

# como la conversión de cadena a flotante puede generar una excepción,
# es mejor continuar con la protección del bloque try-except.
try:
    for substr in strings:  # itera a través de la lista...
        # ... e intenta convertir todos sus elementos en números flotantes
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")


# El código a continuación lo escribí aceptando la sugerencia opcional de esta clase del curso.
print("\n\nLo mismo que antes pero empleando en el código Comprensión de Listas.\n")
line = input("Ingresa una línea de números, sepáralos con espacios: ")
total = 0

try:
    line = [total := total + float(substr) for substr in line.split()]
    print("El total es:", total)
except:
    print(substr, "no es un numero.")

# El siguiente código no se sugiere en el ejemplo d ela clase, pero s eme ocurrió hacerlo utilizando la función eval().
# Esta función aunque está en desuso en Python 3, aún es utilizable. Hice ssto como ejemplo para realizar lo mismo
# utilizando la menor cantidad de líneasd e código posibles.
print("\n\nEl mismo ejemplo pero empleando la función eval().\n")
line = input("Ingresa una línea de números, sepáralos con espacios: ")

try:
    print("El total es:", eval(line.strip().replace(" ", "+")))
except:
    print("Ocurrió un problema. Alguno de los datos escritos no es un numero.")
