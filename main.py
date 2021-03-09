from tkinter import filedialog
from ListaDoble import ListaDoble
from ListaSimple import ListaSimple
import xml.etree.cElementTree as ET
#parsear xml para obtener clases de las cosas

nombre_archivo = None

#declarar listas
Lista1 = ListaSimple()
Lista2 = ListaSimple()
Lista3 = ListaSimple()
Lista4 = ListaSimple()
Lista5 = ListaSimple()
Lista6 = ListaSimple()
Lista7 = ListaSimple()
Lista8 = ListaSimple()
Lista9 = ListaSimple()
ListaN = ListaSimple()
def cargar_archivo():
    global nombre_archivo
    nombre_archivo = nombre_archivo
    file_name = filedialog.askopenfilename()
    try:
        if file_name != None:
            nombre_archivo = file_name
    except:
        print(EOFError)

def proceso_archivo():
    global Lista1, Lista2, Lista3, Lista4, Lista5, Lista6, Lista7, Lista8, Lista9, ListaN
    Lista1 = Lista1
    Lista2 = Lista2
    Lista3 = Lista3
    Lista4 = Lista4
    Lista5 = Lista5
    Lista6 = Lista6
    Lista7 = Lista7
    Lista8 = Lista8
    Lista9 = Lista9
    ListaN = ListaN
    tree = ET.parse(nombre_archivo)
    root = tree.getroot()

    #Recorrer lista de elementos XML
    listaClases = ListaDoble()
    #Clases = etree.xpath('//clase')
    for matriz in root:
        listaClases.insertar(matriz.attrib['nombre'], matriz.attrib['n'], matriz.attrib['m'])
        if matriz.attrib['nombre'] == 'MatrizPrueba1':
            for elemento in matriz:
                Lista1.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'MatrizPrueba2':
            for elemento in matriz:
                Lista2.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'MatrizPrueba3':
            for elemento in matriz:
                Lista3.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'MatrizPrueba4':
            for elemento in matriz:
                Lista4.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'MatrizPrueba5':
            for elemento in matriz:
                Lista5.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'Ejemplo':
            for elemento in matriz:
                Lista6.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'Ejemplo2':
            for elemento in matriz:
                Lista7.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'Ejemplo3':
            for elemento in matriz:
                Lista8.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
        elif matriz.attrib['nombre'] == 'Ejemplo4':
            for elemento in matriz:
                Lista9.insertar(elemento.attrib['x'], elemento.attrib['y'], elemento.text)
                
    Lista6.mostrar()


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
            print('----------- Datos del Estudiante -----------')
            print('Nombre: Juan Francisco Urbina Silva')
            print('Introduccion a la Programacion & Computacion 2 Seccion D')
            print('Carne: 201906051')
            print('Ingenieria en Ciencias & Sistemas')
            print('5to. Semestre')
        elif option == 5:
            print('Generando Grafica')
        elif option == 6:
            print('Fin del Programa')
            break
        else:
            print('Syntax ERROR')

Menprincipal()