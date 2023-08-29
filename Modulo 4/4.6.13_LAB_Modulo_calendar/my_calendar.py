"""
my_calendar -- Elaborado por Rui Duarte dos Santos Melim

Ampliar la funcionalidad de la clase Calendar con un nuevo método llamado count_weekday_in_year, 
que toma un año y un día de la semana como parámetros, y luego devuelve el número de ocurrencias 
de un día de la semana específico en el año.

Consejos:
1.- Crea una clase llamada MyCalendar que se extiende de la clase Calendar.
2.- Crea el método count_weekday_in_year con los parámetros de year y weekday.
El parámetro weekday debe tener un valor entre 0 y 6, donde 0 es el lunes y 6 
es el domingo. El método debe devolver el número de días como un número entero.
3.- Usa el método monthdays2calendar de la clase Calendar.
"""

import calendar


class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        if weekday not in range(7):
            raise ValueError
        count = 0
        for i in range(12):
            for week in super().monthdays2calendar(year, i + 1):
                for day, wday in week:
                    if day != 0:
                        count += 1 if wday == weekday else 0
        return count


year = int(input("Indique el año a evaluar: "))
weekday = int(input("Indique el día de la semana a buscar (0-6): "))
cal = MyCalendar()
print(cal.count_weekday_in_year(year, weekday))
