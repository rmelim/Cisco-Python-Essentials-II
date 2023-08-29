"""
sudoku_test.py -- Elaborado por Rui Duarte dos Santos Melim

Como probablemente sabes, Sudoku es un rompecabezas de colocación de números jugado en un 
tablero de 9x9. El jugador tiene que llenar el tablero de una manera muy específica:

1.- Cada fila del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
2.- Cada columna del tablero debe contener todos los dígitos del 0 al 9 (el orden no importa).
3.- Cada uno de los 9 subcuadros de 3x3 de la tabla debe contener todos los dígitos del 0 al 9.

Si necesitas más detalles, puedes encontrarlos en la Web.

Este es un programa que:

a.- Lee las 9 filas del Sudoku, cada una con 9 dígitos 
(verifica cuidadosamente si los datos ingresados son válidos).
b.- Da como salida "Si" si el Sudoku es válido y "No" de lo contrario.
"""


def verify_1_9(iterable_1_9):
    """Devuelve True si lista_1_9 contienen los valores válidos requeridos"""
    return "".join(sorted(iterable_1_9)) == "123456789"


def verify_sudoku(sudoku):
    """Verifica que el Sudoku cumpla con los requisitos para ser válido"""
    for row in range(9):  # Evalua las filas del Sudoku
        if not verify_1_9(sudoku[row]):
            return False
    for col in range(9):  # Evalua las columnas del Sudoku
        if not verify_1_9([row[col] for row in sudoku]):
            return False
    for row in range(0, 9, 3):  # Contruye y evalua que los subs de 3x3 sean válidos
        for col in range(0, 9, 3):
            sub3x3 = ""
            for sec in range(3):
                sub3x3 += sudoku[sec + row][col:col + 3]
            if not verify_1_9(sub3x3):
                return False
    return True


sudoku_test = []

print("""
      A continuación se le solicitará ingrese las 9 líneas 
      que conforman el Sudoku a verificar. Recuerde que debe 
      escribir 9 dígitos, del 1 al 9, sin importar el orden 
      de los mismos.
      
      Al final, se indicara con un "Si" si el Sudoko es válido.
      De lo contrario se indicará "No".
""")


for i in range(9):
    while True:
        linea = input(f"ingrese la línea No. {i + 1} del Sudoku :")
        if len(linea) == 9 and linea.isdigit():
            sudoku_test.append(linea)
            break
        print("\nLa línea no esta correcta. verifique e intente de nuevo.\n")

print("Si" if verify_sudoku(sudoku_test) else "No")
