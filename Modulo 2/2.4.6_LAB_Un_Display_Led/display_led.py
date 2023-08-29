"""
display_led.py -- Elaborado por Rui Duarte dos Santos Melim

Escribir un programa que puede simular el funcionamiento de un display de siete 
segmentos, aunque va a usar LEDs individuales en lugar de segmentos.

Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), 
así es como lo imaginamos:

  #   ###   ###   # #   ###   ###   ###   ###   ###   ###
  #     #     #   # #   #     #       #   # #   # #   # # 
  #   ###   ###   ###   ###   ###     #   ###   ###   # # 
  #   #       #     #     #   # #     #   # #     #   # # 
  #   ###   ###     #   ###   ###     #   ###   ###   ###

Nota: el número 8 muestra todas las luces LED encendidas.

Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.

Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.
"""


def display(nums):
    """Función que recibe en el parámetro nums un número y sumla un display con él"""
    leds = (("###", "# #", "# #", "# #", "###"),
            ("  #", "  #", "  #", "  #", "  #"),
            ("###", "  #", "###", "#  ", "###"),
            ("###", "  #", "###", "  #", "###"),
            ("# #", "# #", "###", "  #", "  #"),
            ("###", "#  ", "###", "  #", "###"),
            ("###", "#  ", "###", "# #", "###"),
            ("###", "  #", "  #", "  #", "  #"),
            ("###", "# #", "###", "# #", "###"),
            ("###", "# #", "###", "  #", "###"))
    nums = str(nums)
    for i in range(5):
        for num in nums:
            print(leds[int(num)][i], end="  ")
        print()


while True:
    try:
        numero = abs(int(float(input("Escriba un número entero positivo: "))))
        display(numero)
    except ValueError:
        print("Valor inválido. Debe escribir un número entero positivo")
        break
