'''
validador_iban.py

Este programa implementa (en una forma ligeramente simplificada) un algoritmo utilizado por 
los bancos Europeos para especificar los números de cuenta. El estándar llamado IBAN 
(Número de cuenta bancaria internacional) proporciona un método simple y bastante confiable 
para validar los números de cuenta contra errores tipográficos simples que pueden ocurrir durante 
la reescritura del número de documentos en papel, como facturas o facturas en las computadoras.

Un número de cuenta compatible con IBAN consta de:

1.- Un código de país de dos letras tomado del estándar ISO 3166-1 
(por ejemplo, FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).

2.- Dos dígitos de verificación utilizados para realizar las verificaciones de validez: 
pruebas rápidas y simples, pero no totalmente confiables, que muestran si un número es inválido 
(distorsionado por un error tipográfico) o válido.

3.- El número de cuenta real (hasta 30 caracteres alfanuméricos; la longitud depende del país).


El estándar dice que la validación requiere los siguientes pasos (según Wikipedia):

(Paso 1) Verifica que la longitud total del IBAN sea correcta según el país 
(este programa no lo hará, pero puedes modificarlo para cumplir con este requisito 
si lo deseas; pero debes enseñar al código a conocer todas las longitudes utilizadas en Europa).

(Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena 
(es decir, el código del país y los dígitos de verificación).

(Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena, 
donde A = 10, B = 11 ... Z = 35.

(Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número dividiéndolo 
entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos y el IBAN puede ser válido.
'''

# Pide al usuario que ingrese el IBAN (el número puede contener espacios, ya que mejoran
# significativamente la legibilidad del número...
iban = input("Ingresa un IBAN, por favor: ")
iban = iban.replace(' ', '')  # ... pero remueve los espacios de inmediato).

# el IBAN ingresado debe constar solo de dígitos y letras, de lo contrario...
if not iban.isalnum():
    print("Has introducido caracteres no válidos.")  # ... muestra un mensaje.
elif len(iban) < 15:  # el IBAN no debe tener menos de 15 caracteres (esta es la variante más corta, utilizada en Noruega)
    # si es más corto, se informa al usuario.
    print("El IBAN ingresado es demasiado corto.")
# además, el IBAN no puede tener más de 31 caracteres (esta es la variante más larga, utilizada en Malta).
elif len(iban) > 31:
    # si es más largo, se le informa al usuario.
    print("El IBAN ingresado es demasiado largo.")
else:  # se comienza con el procesamiento.
    # se mueven los cuatro caracteres iniciales al final del número y se convierten
    # todas las letras a mayúsculas (paso 02 del algoritmo).
    iban = (iban[4:] + iban[0:4]).upper()
    # esta es la variable utilizada para completar el número, creada al reemplazar
    # las letras con dígitos (de acuerdo con el paso 03 del algoritmo).
    iban2 = ''
    for ch in iban:  # iterar a través del IBAN.
        if ch.isdigit():  # si el carácter es un dígito...
            iban2 += ch  # solo se copia.
        else:  # de lo contrario...
            # ... conviértelo en dos dígitos
            iban2 += str(10 + ord(ch) - ord('A'))
    # la forma convertida del IBAN está lista: ahora se convierte en un número entero.
    iban = int(iban2)
    if iban % 97 == 1:  # ¿si el residuo de iban2 entre 97 es igual a 1?
        # entonces el número es correcto.
        print("El IBAN ingresado es válido.")
    else:  # de lo contrario...
        # ... el número no es válido.
        print("El IBAN ingresado no es válido.")


# Aquí algunos datos de prueba (todos estos números son válidos;
# puedes invalidarlos cambiando cualquier carácter).

# Inglés: GB72 HBZU 7006 7212 1253 00
# Francés: FR76 30003 03620 00020216907 50
# Alemán: DE02100100100152517108

# Si eres residente de la UE, puedes usar tu propio número de cuenta para hacer pruebas.
