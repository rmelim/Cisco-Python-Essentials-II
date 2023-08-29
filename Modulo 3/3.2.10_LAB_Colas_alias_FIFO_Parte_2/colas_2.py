"""
colas_2.py -- Elaborado por Rui Duarte dos Santos Melim

Aquí se va a extender ligeramente las capacidades de la clase Queue 
que está en 3.2.9_LAB_Colas_alias_FIFO. Queremos que tenga un método 
sin parámetros que devuelva True si la cola está vacía y False de lo contrario.
"""


class QueueError(IndexError):
    def __init__(self):
        pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if len(self.queue) == 0:
            raise QueueError
        val = self.queue[0]
        del self.queue[0]
        return val


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return len(self.queue) == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
