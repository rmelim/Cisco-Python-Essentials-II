"""
point.py -- Elaborado por Rui Duarte dos Santos Melim

Plano con el sistema de coordenadas cartesianas. Cada punto ubicado en el plano puede 
describirse como un par de coordenadas habitualmente llamadas X y Y. 

Clase en Python que almacene ambas coordenadas como números flotantes. Además, los objetos 
de esta clase evalúen las distancias entre cualquiera de los dos puntos situados en el plano.

Se emplea la función denominada hypot() (disponible a través del módulo math) que evalúa la 
longitud de la hipotenusa de un triángulo rectángulo.

la clase:

1.- Se llama Point.

2.- Su constructor acepta dos argumentos (X y Y respectivamente), ambos por defecto se igualan 
a cero.

3.- Todas las propiedades deben ser privadas.

4.- La clase contiene dos métodos sin parámetros llamados getx() y gety(), que devuelven cada 
una de las dos coordenadas (las coordenadas se almacenan de forma privada, por lo que no se 
puede acceder a ellas directamente desde el objeto).

5.- La clase proporciona un método llamado distance_from_xy(x,y), que calcula y devuelve la 
distancia entre el punto almacenado dentro del objeto y el otro punto dado en un par de números 
flotantes.

6.- La clase proporciona un método llamado distance_from_point(point), que calcula la distancia 
(como el método anterior), pero la ubicación del otro punto se da como otro objeto de clase Point.
"""

import math


class Point:
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


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
