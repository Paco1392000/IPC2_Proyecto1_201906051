from Dato import Dato
class ListaSimple:
    def __init__(self):
        self.inicio = None

    #inserta el nuevo objeto
    def insertar(self, x, y, name):
        nuevo = Dato(x, y, name)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while True:
                if tmp.siguiente == None:
                    break
                else:
                    tmp = tmp.siguiente
            tmp.siguiente = nuevo

    #muestra el objeto
    def mostrar(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + ' [x: ' + str(tmp.x) + '. y: ' + str(tmp.y) + ']' + ' - Dato: ' + str(tmp.name) +'\t' )
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
            if str.lower(tmp.name) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None

    def bus_Pos(self, f, c):
        aux = self.inicio
        while True:
            if aux.x == f and aux.y == c:
                return aux.name
            if aux.siguiente == None:
                break
            else:
                aux = aux.siguiente
        return None