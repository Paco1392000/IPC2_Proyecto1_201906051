from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from ElementTree_pretty import prettify
import xml.etree.cElementTree as ET
from tkinter import filedialog
from graphviz import Digraph
from xml.dom import minidom
from Lista import Lista

class main():
    def __init__(self):
        self.link = None
        self.nombre_archivo = None
        self.matriz = Lista()


    def cargar_archivo(self):
        file_name = filedialog.askopenfilename()
        try:
            if file_name != None:
                self.nombre_archivo = file_name
        except:
            print(EOFError)

    def datos_estudiante(self):
        print('----------- Datos del Estudiante -----------')
        print('Nombre: Juan Francisco Urbina Silva')
        print('Introduccion a la Programacion & Computacion 2 Seccion D')
        print('Carne: 201906051')
        print('Ingenieria en Ciencias & Sistemas')
        print('5to. Semestre')

    def proceso_archivo(self):
        global matriz, link
        matriz = matriz
        link = link
        tree = ET.parse(nombre_archivo)
        root = tree.getroot()

        #Recorrer lista de elementos XML
        
        #Clases = etree.xpath('//clase')
        
            


    def Menprincipal(self):
        option = 0
        while option != 7:
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
                exit()
            else:
                print('Syntax ERROR')
                exit()
    
iniciar = main()
iniciar.Menprincipal()        


