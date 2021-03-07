from Matriz import Matriz
class ListaDoble:
    def __init__(self):
        self.inicio = None

    #insertar elementos
    def insertar(self, nombre, n, m):#atributos de la clase
        nuevo = Matriz(nombre, n, m)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp
    
    #muestra
    def mostrar(self):
        tmp = self.inicio
        contador = 1
        while tmp is not None:
            print(str(contador) + '. Nombre: ' + str(tmp.nombre) + '. n: ' + str(tmp.n) + '. m: ' + str(tmp.m))
            print('Algo Registrado: ' + str(tmp.mat.getSize()))#Tamaño de la Lista
            contador += 1
            tmp = tmp.siguiente
    
    #Tamaño
    def getSize(self):
        tmp = self.inicio
        cont = 0
        while tmp is not None:
            cont += 1
            tmp = tmp.siguiente
        return cont

    #busqueda & retorno
    def getNodo(self, valor):
        tmp = self.inicio
        while tmp is not None:
            if str.lower(tmp.nombre) == str.lower(valor):
                return tmp
            tmp = tmp.siguiente
        return None