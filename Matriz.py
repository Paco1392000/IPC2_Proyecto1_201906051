from ListaSimple import ListaSimple
class Matriz:
    def __init__(self, nombre, n, m):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.mat = ListaSimple()
        self.siguiente = None
        self.anterior = None