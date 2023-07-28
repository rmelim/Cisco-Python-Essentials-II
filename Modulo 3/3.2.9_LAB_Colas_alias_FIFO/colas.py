"""
colas.py

Como ya sabes, una pila es una estructura de datos que realiza el modelo LIFO 
(último en entrar, primero en salir).

Probemos ahora una cola (queue), es un modelo de datos caracterizado por el término FIFO: 
primero en entrar, primero en salir. Nota: una cola (fila) regular que conozcas de las tiendas 
u oficinas de correos funciona exactamente de la misma manera: un cliente que llegó primero 
también es el primero en ser atendido.

Tu tarea es implementar la clase Queue con dos operaciones básicas:

1.- put(elemento), que coloca un elemento al final de la cola.
2.- get(), que toma un elemento del principio de la cola y lo devuelve como resultado 
(la cola no puede estar vacía para realizarlo correctamente).

Sigue las sugerencias:

a.- Emplea una lista como tu almacenamiento.
b.- put() debe agregar elementos al principio de la lista, 
mientras que get() debe eliminar los elementos del final de la lista.
c.- Define una nueva excepción llamada QueueError (elige una excepción de la cual se derivará) 
y generala cuando get() intente operar en una lista vacía.
"""


class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    def __init__(self):
        pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError
        val = self.__queue[0]
        del self.__queue[0]
        return val


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")
