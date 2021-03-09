from tkinter import filedialog
from xml.dom import minidom
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
from xml.etree.ElementTree import Comment
from Lista import Lista
import xml.etree.cElementTree as ET

link = None
nombre_archivo = None
matriz = Lista()


def cargar_archivo():
    global nombre_archivo
    nombre_archivo = nombre_archivo
    file_name = filedialog.askopenfilename()
    try:
        if file_name != None:
            nombre_archivo = file_name
    except:
        print(EOFError)

def datos_estudiante():
    print('----------- Datos del Estudiante -----------')
    print('Nombre: Juan Francisco Urbina Silva')
    print('Introduccion a la Programacion & Computacion 2 Seccion D')
    print('Carne: 201906051')
    print('Ingenieria en Ciencias & Sistemas')
    print('5to. Semestre')

def proceso_archivo():
    
    
    tree = ET.parse(nombre_archivo)
    root = tree.getroot()

    #Recorrer lista de elementos XML
    listaClases = ListaDoble()
    #Clases = etree.xpath('//clase')
    for matriz in root:
        listaClases.insertar(matriz.attrib['nombre'], matriz.attrib['n'], matriz.attrib['m'])
        if matriz.attrib['nombre'] != None:
            for elemento in matriz:
                matriz.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        


def Menprincipal():
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
            cargar_archivo()
            print('Cargando Archivo')
            print('Archivo Cargado')
        elif option == 2:
            print('Procesando Archivo')
            proceso_archivo()
        elif option == 3:
            print('Escribiendo el Archivo de Salida')
        elif option == 4:
            datos_estudiante()
        elif option == 5:
            print('Generando Grafica')
        elif option == 6:
            print('Fin del Programa')
            break
        else:
            print('Syntax ERROR')

Menprincipal()
    


