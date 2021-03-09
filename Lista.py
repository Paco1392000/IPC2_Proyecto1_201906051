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
    def ingresarValores(self, dato, x, y): 
        tmp = Nodo(dato, x, y)
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

    def Dev(self, parte):
        aux = self.inicio
        cnt = 1
        while cnt < parte:
            cnt += 1
            aux = aux.siguiente
        return aux
    def borrarFila(self, parte):
        self.Dev(parte - 1).siguiente = self.Dev(parte + 1)
        self.large -= 1

    def largo(self):
        return self.large
    
    def NodoMostrado(self):
        aux = self.inicio
        ta = 0
        while ta < self.large:
            ta += 1
            print(' .-. ' + str(aux.nombre) + ' .-. ')
            aux = aux.siguiente

    def ListaVacia(self):
        self.inicio = None
    
    def CListaVacia(self):
        cv = True
        if self.large == 0:
            return cv
        else:
            cv = False
            return False