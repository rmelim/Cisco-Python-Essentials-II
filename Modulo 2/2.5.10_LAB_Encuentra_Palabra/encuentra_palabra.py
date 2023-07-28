"""
encuentra_palabra.py

Vamos a jugar un juego. Te daremos dos cadenas: una es una palabra (por ejemplo, "dog") 
y la segunda es una combinación de un grupo de caracteres.

Este es un programa que responda la siguiente pregunta: 
¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?

Por ejemplo:
Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si;
Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no 
(ya que no están las letras "d", "o", o "g" ni en ese orden)

Pistas:
1.- Debes usar las variantes de dos argumentos de las funciones pos() dentro de tu código.
2.- No te preocupes por mayúsculas y minúsculas.
    """


def find_word(word, string):
    """ Encuenta word dentro de string """
    total_char = len(word)
    string = list(string)
    for char in word:
        try:
            pos = string.index(char)
            total_char -= 1
            del string[:pos + 1]
        except ValueError:
            continue
    return "Si" if total_char == 0 else "No"


palabra = input("Escribe una palabra: ").lower()
cadena = input("Escribe la una cadena de carateres: ").lower()

print(f"La palabra {palabra} {find_word(palabra, cadena)} está en {cadena}")
