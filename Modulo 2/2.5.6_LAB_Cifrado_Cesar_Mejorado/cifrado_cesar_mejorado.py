'''
cifrado_cesar_mejorado.py

El cifrado César original cambia cada carácter por otro: a se convierte en b, z se convierte en a, 
y así sucesivamente. Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga 
del rango 1..25.

Además, dejemos que el código conserve las mayúsculas y minúsculas y todos los caracteres no 
alfabéticos deben permanecer intactos.

El programa debe hacer lo siguiente:

1.- Le pida al usuario una línea de texto para encriptar.

2.- Le pida al usuario un valor de cambio (un número entero del rango 1..25) 
nota: debes obligar al usuario a ingresar un valor de cambio válido.

3.- Imprime el texto codificado.
'''

text = input("Ingresa el mensaje a encriptar: ")
while True:
    valor_cambio = int(input("Ingrese un valor de codificación (1 a 25): "))
    if 1 <= valor_cambio <= 25:
        break
    print("\nIngrese un valor válido de 1 a 25\n")

cipher = ''

for char in text:
    code = ord(char)
    if char.isalpha():
        code += valor_cambio
        if char.islower():
            if code > ord('z'):
                code = (code - ord('z')) + ord('a') - 1
        else:
            if code > ord('Z'):
                code = (code - ord('Z')) + ord('A') - 1
    cipher += chr(code)

print(cipher)
