"""
timer.py -- Elaborado por Rui Duarte dos Santos Melim

Clase que se llama Timer (temporizador en español). Su constructor acepta tres argumentos 
que representan horas (un valor del rango [0..23]; usaremos tiempo militar), minutos (del 
rango [0. .59]) y segundos (del rango [0..59]).

Cero es el valor predeterminado para todos los parámetros anteriores. No es necesario realizar 
ninguna comprobación de validación.

La clase en sí debería proporcionar las siguientes facilidades:

1.- Los objetos de la clase deben ser "imprimibles", es decir, deben poder convertirse implícitamente 
en cadenas de la siguiente forma: "hh:mm:ss", con ceros a la izquierda agregados cuando cualquiera de 
los valores es menor que 10.

2.- La clase debe estar equipada con métodos sin parámetros llamados next_second() y previous_second(), 
incrementando el tiempo almacenado dentro de los objetos en +1/-1 segundos respectivamente.

Emplea las siguientes sugerencias:

a.- Todas las propiedades del objeto deben ser privadas.
b.- Considera escribir una función separada (¡no un método!) para formatear la cadena con el tiempo.
"""


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        hour = str(self.__hours).zfill(2)
        minute = str(self.__minutes).zfill(2)
        second = str(self.__seconds).zfill(2)
        return f"{hour}:{minute}:{second}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
