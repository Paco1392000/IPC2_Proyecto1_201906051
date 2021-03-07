from Algo import Algo
class ListaSimple:
    def __init__(self):
        self.inicio = None

    #inserta el nuevo objeto
    def insertar(self, nombre, n, m):
        nuevo = Algo(nombre, n, m)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
        tmp.siguiente = nuevo

    #muestra el objeto
    def mostrar(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '. Nombre: ' + str(tmp.nombre) + '. N: ' + str(tmp.n) + '. M: ' + str(tmp.m) + '\n')
            contador += 1
            tmp = tmp.siguiente
    
    #Longitud o tamaño
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont
    
    #busqueda y retorno
    def getNodo(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None
