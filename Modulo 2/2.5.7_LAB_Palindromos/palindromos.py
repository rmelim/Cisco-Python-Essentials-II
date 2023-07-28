"""
palindromos.py

Un palíndromo es una palabra que se ve igual cuando se lee hacia adelante y hacia atrás. 
Por ejemplo, "kayak" es un palíndromo, mientras que "leal" no lo es.

Este es un programa que:

1.- Le pida al usuario algún texto.
2.- Compruebe si el texto introducido es un palíndromo e imprima el resultado.

Nota:
a.- Supón que una cadena vacía no es un palíndromo.
b.- Trata a las letras mayúsculas y minúsculas como iguales.
c.- Los espacios no se toman en cuenta durante la verificación: trátalos como inexistentes.
"""


def no_space(texto):
    """ Elimina los espacios en blanco para no tomarlos en cuenta """
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    """ Revierte todo el texto"""
    texto = no_space(texto)
    invert = ""
    for char in texto:
        invert = char + invert
    return invert


def es_palindromo(texto):
    """ Verifica si el texto normal y revertido son iguales"""
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto_al_reves.lower() == texto.lower()


mi_texto = input("Escriba una línea de texto: ")
if mi_texto.strip() != "" and es_palindromo(mi_texto):
    print("El texto escrito es un palíndromo: ", reverse(mi_texto))
else:
    print("El texto escrito no es un palíndromo")
