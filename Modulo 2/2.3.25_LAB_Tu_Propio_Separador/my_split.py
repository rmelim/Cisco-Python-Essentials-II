'''
my_split.py -- Elaborado por Rui Duarte dos Santos Melim

Escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

1.- Debe aceptar únicamente un argumento: una cadena.
2.- Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares
    donde la cadena contiene espacios en blanco.
3.- Si la cadena está vacía, la función debería devolver una lista vacía.
4.- Su nombre debe ser mysplit().
'''


def mysplit(string):
    string = string.strip()
    result = []
    if string != '':
        word = ''
        string += ' '
        for char in string:
            if char != ' ':
                word += char
            else:
                result.append(word)
                word = ''
    return result


print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
