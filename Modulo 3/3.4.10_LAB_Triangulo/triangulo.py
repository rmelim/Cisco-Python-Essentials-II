"""
triangulo.py -- Elaborado por Rui Duarte dos Santos Melim

Ahora vamos a colocar la clase Point (ver Lab anterior) dentro de otra clase. 
Además, vamos a poner tres puntos en una clase, lo que nos permitirá definir un triángulo.

La nueva clase se llamará Triangle y esto es lo que queremos:

1.- El constructor acepta tres argumentos - todos ellos son objetos de la clase Point.

2.- Los puntos se almacenan dentro del objeto como una lista privada.

3.- La clase proporciona un método sin parámetros llamado perimeter(), que calcula el 
perímetro del triángulo descrito por los tres puntos; suma de todas las longitudes de 
los lados.
"""

import math


class Point:  # Clase que se definió en el LAB 3.4.9
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(x - self.getx(), y - self.gety())

    def distance_from_point(self, point):
        return math.hypot(point.getx() - self.getx(), point.gety() - self.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        result = 0
        for i in range(3):
            result += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return result


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
