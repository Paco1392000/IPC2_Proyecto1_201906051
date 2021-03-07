from tkinter import filedialog
from ListaDoble import ListaDoble
from ListaSimple import ListaSimple
import xml.etree.cElementTree as ET

class MatrizNodo():
    def __init__(self, fila, columna, valor):
        self.valor = valor
        self.fila = fila
        self.columna = columna
        self.siguiente = None

class ListaMat():
    def __init__(self):
        self.inicio = None

    def agregarValor(self, fila, columna, valor):
        temp = MatrizNodo(fila, columna, valor)
        if self.inicio == None:
            self.inicio = temp
        else:
            aux = self.inicio
            while True:
                if aux.siguiente == None:
                    break
                else:
                    aux = aux.siguiente
            aux.siguiente = temp

    def getPos(self, fila, columna):
        aux = self.inicio
        while True:
            if aux.fila == fila and aux.columna == columna:
                return aux.valor
            if aux.siguiente == None:
                break
            else:
                aux = aux.siguiente
        return None

n = 2
m = 3
obj = ListaMat()
obj.agregarValor(1,1,15)
obj.agregarValor(1,2,21)
obj.agregarValor(1,3,16)
obj.agregarValor(2,1,14)
obj.agregarValor(2,2,12)
obj.agregarValor(2,3,1)

for i in range(0,n):
    p = ""
    for j in range(0,m):
        p = p + str(obj.getPos(i+1,j+1))+ "\t"
    print(p)