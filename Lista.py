from Nodo import Nodo
class Lista:
    def __init__(self):
        self.large = 0
        self.binabi = ''
        self.camb = False
        self.inicio = None

    def agregar(self, dato):
        tmp = Nodo(dato)
        if self.inicio is None:
            self.inicio = tmp
            self.inicio.siguiente = self.inicio
            self.large += 1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1
            else:
                aux = self.inicio
                while aux.siguiente != self.inicio:
                    aux = aux.siguiente
                aux.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1

    def ingresarValores(self, x, y, dato):
        tmp = Nodo(x, y, dato)
        if self.inicio is None:
            self.inicio = tmp
            self.inicio.siguiente = self.inicio
            self.large += 1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1
            else:
                aux = self.inicio
                while aux.siguiente != self.inicio:
                    aux = aux.siguiente
                aux.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1

    def AgregarLista(self, dato):
        tmp = dato
        if self.inicio is None:
            self.inicio = tmp
            self.inicio.siguiente = self.inicio
            self.large += 1
        else:
            if self.inicio.siguiente == self.inicio:
                self.inicio.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1
            else:
                aux = self.inicio
                while aux.siguiente != self.inicio:
                    aux = aux.siguiente
                aux.siguiente = tmp
                tmp.siguiente = self.inicio
                self.large += 1

    