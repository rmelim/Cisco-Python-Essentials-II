'''
cifrado_cesar_simple.py

Este cifrado fue (probablemente) inventado y utilizado por Cayo Julio César y sus tropas 
durante las Guerras Galas. La idea es bastante simple: cada letra del mensaje se reemplaza 
por su consecuente más cercano (A se convierte en B, B se convierte en C, y así sucesivamente). 
La única excepción es la Z, la cual se convierte en A.

El programa en el editor es una implementación muy simple (pero funcional) del algoritmo.
'''

# pide al usuario que ingrese un mensaje (sin cifrar) de una línea.
text = input("Ingresa tu mensaje: ")
# prepara una cadena para el mensaje cifrado (esta vacía por ahora).
cipher = ''

for char in text:  # inicia la iteración a través del mensaje.
    if not char.isalpha():  # si el carácter actual no es alfabético...
        continue           # ...ignorala.
    char = char.upper()  # convierta la letra a mayúsculas
    # obtén el código de la letra e increméntalo en uno.
    code = ord(char) + 1
    # si el código resultante ha "dejado" el alfabeto latino (mayor que Z)...
    if code > ord('Z'):
        code = ord('A')  # ... cámbialo al código de la A.
    # agrega el carácter recibido al final del mensaje cifrado.
    cipher += chr(code)

print(cipher)
