"""
enteros_seguros.py

FGunción capaz de ingresar valores enteros y verificar si están dentro de un rango 
especificado.

La función deberá:

1.- Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite 
superior aceptable.
2.- Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir 
el mensaje Error: entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
3.- Si el usuario ingresa un número que está fuera del rango especificado, la función debe 
emitir el mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará 
al usuario que ingrese el valor nuevamente.
4.- Si el valor de entrada es válido, será regresado como resultado.
"""


def read_int(prompt, min, max):
    while True:
        try:
            result = int(input(prompt))
            assert min <= result <= max
            return result
        except ValueError:
            print("Error: entrada incorrecta")
            continue
        except AssertionError:
            print("Error: el valor no está dentro del rango permitido (-10..10)")
            continue


v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)

print("El número es:", v)
