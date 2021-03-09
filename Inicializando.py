from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from ElementTree_pretty import prettify
import xml.etree.cElementTree as ET
from tkinter import filedialog
from graphviz import Digraph
from xml.dom import minidom
from Lista import Lista
import os
class Inicializando():
    def __init__(self):
        self.gate = None
        self.matrix = Lista()
    def cargar_archivo(self):
        try:
            file_name = filedialog.askopenfilename()
            rut = minidom.parse(file_name)
            self.gate = rut
        except:
            print('Error')
    def datos_estudiante(self):
        print('----------- Datos del Estudiante -----------')
        print('Nombre: Juan Francisco Urbina Silva')
        print('Introduccion a la Programacion & Computacion 2 Seccion D')
        print('Carne: 201906051')
        print('Ingenieria en Ciencias & Sistemas')
        print('5to. Semestre')
    def proceso_archivo(self):
        ifes = self.gate.getElementsByTagName('matriz')    
        contador = 1
        for matriz in ifes:
            fila = matriz.getAttribute('n')
            columna = matriz.getAttribute('m')
            self.matrix.ingresarValores(matriz.attributes['nombre'].value, fila, columna)            
            filas = Lista()
            for a in range(int(fila)):
                filax = Lista()
                filas.AgregarLista(filax)
            datos = matriz.getElementsByTagName('dato')
            for dato in datos:
                x = int(dato.attributes['x'].value)
                valor = dato.firstChild.data
                filas.Dev(x).agregar(valor)
                if int(valor) == 0:
                    filas.Dev(x).binabi += '0'
                else:
                    filas.Dev(x).binabi += '1'
            self.matrix.Dev(contador).matriz= filas
            contador+=1                            
            print('Datos Cargados')
        for a in range(self.matrix.large):            
            ConverBinario = False #binarioFlag
            print('Obteniendo Matriz Binaria')            
            datore = Lista()
            datore.ListaVacia()
            reduccion = Lista()
            reduccion.ListaVacia()


            for i in range(self.matrix.Dev(a + 1).matriz.large):
                repeticion = Lista()                                
                repeticion.ListaVacia()
                newFila = Lista()
                newFila.ListaVacia()
                for j in range(self.matrix.Dev(a+1).matriz.large):
                    if (i+1)!=(j+1):
                        if self.matrix.Dev(a+1).matriz.Dev(i + 1).binabi == self.matrix.Dev(a+1).matriz.Dev(j + 1).binabi and self.matrix.Dev(a+1).matriz.Dev(i+1).camb == False and self.matrix.Dev(a+1).matriz.Dev(j+1).camb == False:
                            if repeticion.esVacia()==True:
                                repeticion.agregar(i + 1)
                                repeticion.agregar(j + 1)
                                self.matrix.Dev(a + 1).matriz.Dev(j + 1).camb = True
        
                                for p in range(self.matrix.Dev(a+1).matriz.Dev(i+1).large):
                                    valor = int(self.matrix.Dev(a+1).matriz.Dev(i+1).Dev(p+1).nombre) + int(self.matrix.Dev(a+1).matriz.Dev(j+1).Dev(p+1).nombre)
                                    newFila.agregar(valor)
                            else:
                                repeticion.agregar(j+1)
                                self.matrix.Dev(a+1).matriz.Dev(j+1).camb = True
                                for p in range(self.matrix.Dev(a+1).matriz.Dev(i+1).large):
                                    newFila.Dev(p+1).nombre += int(self.matrix.Dev(a+1).matriz.Dev(j+1).Dev(p+1).nombre)
                if repeticion.CListaVacia() == False:
                    repeticiones.AgregarLista(repeticion)
                    reduccion.AgregarLista(newFila)
            self.matrix.Dev(a+1).datore = datore
            self.matrix.Dev(a+1).redmat = reduccion
            if datore.CListaVacia() == False:
                contador = 0
                for k in range(self.matrix.Dev(a+1).matriz.large):
                    camb = False
                    for t in range(datore.large):
                        for b in range(datore.Dev(t+1).large):
                            if k + 1 == datore.Dev(t+1).Dev(b+1).nombre:
                                camb = True
                    if camb == False:
                        newfila = Lista()
                        newfila.ListaVacia()
                        for u in range(self.matrix.Dev(a+1).matriz.Dev(k+1).large):
                            newfila.insertar(self.matrix.Dev(a+1).matriz.Dev(k+1).Dev(u+1).nombre)
                        self.matrix.Dev(a+1).redmat.AgregarLista(newfila)
                        contador+=1

            for s in range(contador):
                listita = Lista()
                listita.agregar(1)
                self.matrix.Dev(a+1).datore.AgregarLista(listita)
            for n in range(self.matrix.Dev(a+1).redmat.large):
                print('No. '+ str(n+1))
                self.matrix.Dev(a+1).redmat.Dev(n+1).NodoMostrado()
        print('Proceso terminado, presione ENTER para continuar')       


        


    def Menuprincipal(self):
        fuera = False
        while fuera == False:
            try:
                print('-------- Menu Principal --------')
                print('1. Cargar Archivo')
                print('2. Procesar Archivo')
                print('3. Crear Archivo de Salida')
                print('4. Mostrar Datos del Estudiante')
                print('5. Generar Grafica')
                print('6. Salir')
                option = int(input('Ingresar Opcion: '))
                if option == 1:
                    self.cargar_archivo()
                    print('Cargando Archivo')
                    print('Archivo Cargado')
                elif option == 2:
                    print('Procesando Archivo')
                    self.proceso_archivo()
                elif option == 3:
                    print('Escribiendo el Archivo de Salida')
                elif option == 4:
                    self.datos_estudiante()
                elif option == 5:
                    print('Generando Grafica')
                elif option == 6:
                    print('Fin del Programa')
                    fuera = True
                else:
                    print('Syntax ERROR')
                    exit()
            except:
                print('Error')
       

empezar = Inicializando()
empezar.Menuprincipal()
