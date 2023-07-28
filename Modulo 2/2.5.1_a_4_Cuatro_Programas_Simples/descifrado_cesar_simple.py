'''
descifrado_cesar_simple.py

La operación inversa a lopresentado en el programa cifrado_cesar_simple.py, ek cual debería ser 
claro para quien lo lea: solo presentamos el código tal como está, sin ninguna explicación.

Observa el código en el editor. Comprueba cuidadosamente si funciona. 
Usa el criptograma del programa cifrado_cesar_simple.py.
'''

cipher = input('Ingresa tu criptograma: ')
text = ''

for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)
