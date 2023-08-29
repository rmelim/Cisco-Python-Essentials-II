"""
anagramas.py -- Elaborado por Rui Duarte dos Santos Melim

Un anagrama es una nueva palabra formada al reorganizar las letras de una palabra, usando 
todas las letras originales exactamente una vez. Por ejemplo, las frases "rail safety" y 
"fairy tales" son anagramas, mientras que "I am" y "You are" no lo son.

Este es un programa que:

1.- Le pide al usuario dos textos por separado.
2.- Comprueba si los textos ingresados son anagramas e imprima el resultado.

Nota:
a.- Supongamos que dos cadenas vacías no son anagramas.
b.- Tratar a las letras mayúsculas y minúsculas como iguales.
c.- Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
"""

texto1 = input("Escriba el primer texto: ")
texto2 = input("Escriba el segundo texto: ")

texto1 = texto1.replace(" ", "").lower()
texto2 = texto2.replace(" ", "").lower()

texto1 = sorted(texto1)
texto2 = sorted(texto2)

if len(texto1) > 1 and len(texto2) > 1 and texto1 == texto2:
    print("Anagramas")
else:
    print("No son anagramas")
