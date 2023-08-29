"""
weeker.py -- Elaborado por Rui Duarte dos Santos Melim

Implementa una clase llamada Weeker. Sí, tus ojos no te engañan, este nombre proviene del 
hecho de que los objetos de esta clase podrán almacenar y manipular los días de la semana.

El constructor de la clase acepta un argumento: una cadena. La cadena representa el nombre 
del día de la semana y los únicos valores aceptables deben provenir del siguiente conjunto:

Lun Mar Mie Jue Vie Sab Dom

Invocar al constructor con un argumento desde fuera de este conjunto debería generar la excepción 
WeekDayError (defínela tu mismo). La clase debe proporcionar las siguientes facilidades:

1.- Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente 
en cadenas de la misma forma que los argumentos del constructor.

2.- La clase debe estar equipada con métodos de un parámetro llamados add_days(n) y subtract_days(n), 
siendo n un número entero que actualiza el día de la semana almacenado dentro del objeto mediante el 
número de días indicado, hacia adelante o hacia atrás.

3.- Todas las propiedades del objeto deben ser privadas.
"""


class WeekDayError(Exception):
    pass


class Weeker:
    __days = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

    def __init__(self, day):
        if day not in Weeker.__days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, n):
        self.__day = Weeker.__days[Weeker.__days.index(self.__day) + (n % 7)]

    def subtract_days(self, n):
        self.__day = Weeker.__days[Weeker.__days.index(self.__day) - (n % 7)]


try:
    weekday = Weeker('Lun')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Lunes')
except WeekDayError:
    print("Lo siento, no puedo atender tu solicitud.")
