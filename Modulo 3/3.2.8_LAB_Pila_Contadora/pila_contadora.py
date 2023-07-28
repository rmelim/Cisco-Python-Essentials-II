"""
pila_contadora.py

Extender el comportamiento de la clase Stack de tal manera que la clase pueda contar 
todos los elementos que son agregados (push) y quitados (pop).

Sugerencias:

1.- Introduce una propiedad diseñada para contar las operaciones pop y nombrarla de una 
manera que garantice que esté oculta.
2.- Inicializala a cero dentro del constructor.
3.- Proporciona un método que devuelva el valor asignado actualmente al contador 
(nómbralo get_counter()).
"""


class Stack:
    """Clase que crea una pila"""

    def __init__(self):
        self.__stk = []

    def push(self, val):
        """Método para colocar valores en la pila"""
        self.__stk.append(val)

    def pop(self):
        """Método para quitar valores de la pila"""
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    """Clase que implementa cambios a partir de Stack"""

    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        """Método que devuelve la cantidad de pop() que se hayan ejecutado"""
        return self.__counter

    def pop(self):
        self.__counter += 1
        return Stack.pop(self)


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
