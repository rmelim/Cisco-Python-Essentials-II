"""
digito_vida.py

Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. 
Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de 
un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

1 Enero 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 es el dígito que buscamos y encontramos.

Este es un programa que:

1.- Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA; 
en realidad, el orden de los dígitos no importa).
2.- Da como salida El Dígito de la Vida para la fecha ingresada.
"""

fecha_nac = input("Escriba su fecha de nacimiento (formato: AAAAMMDD): ")

if fecha_nac.isdigit():
    while True:
        digito_vida = 0
        for digito in fecha_nac:
            digito_vida += int(digito)
        if digito_vida > 10:
            fecha_nac = str(digito_vida)
        else:
            break
    print("El dígito de la vida es:", digito_vida)
else:
    print("Formato inválido.")
