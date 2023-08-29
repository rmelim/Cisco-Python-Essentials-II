"""
strftime_test.py -- Elaborado por Rui Duarte dos Santos Melim

Programa que cree un objeto datetime para el 4 de noviembre de 2020, 14:53:00. 
El objeto creado debe llamar al método strftime con el formato apropiado para 
mostrar el siguiente resultado:

2020/11/04 14:53:00
20/November/04 14:53:00 PM
Wed, 2020 Nov 04
Wednesday, 2020 November 04
Día de la semana: 3
Día del año: 309
Número de semana en el año: 44

Nota:
Cada línea de resultado debe crearse llamando al método strftime con al menos una 
directiva en el argumento de formato.
"""

from datetime import datetime

dt = datetime(2020, 11, 4, 14, 53)

print(dt.strftime("%Y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Dia de la semana: %w"))
print(dt.strftime("Dia del año: %j"))
print(dt.strftime("Número de semana en el año: %U"))
