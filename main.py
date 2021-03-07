from tkinter import filedialog
from ListaDoble import ListaDoble
from ListaSimple import ListaSimple
import xml.etree.cElementTree as ET

#parsear xml para obtener clases de las cosas
tree = ET.parse('Matriz2.xml')
root = tree.getroot()

#declarar listas
ListaNueva = ListaSimple()

#Recorrer lista de elementos XML
for elemento in root:
    if elemento.attrib['nombre'] == 'Ejemplo':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
    elif elemento.attrib['nombre'] == 'MatrizPrueba1':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
    elif elemento.attrib['nombre'] == 'MatrizPrueba2':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
    elif elemento.attrib['nombre'] == 'Ejemplo1':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
    elif elemento.attrib['nombre'] == 'Ejemplo2':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
    else:
        print('Error')
            
listaClases = ListaDoble()
#Clases = etree.xpath('//clase')
for matriz in root:
    listaClases.insertar(matriz.attrib['nombre'], matriz.attrib['n'], matriz.attrib['m'])

print('lista de clases de cosas sin cosas')
listaClases.mostrar()
listamad = listaClases.getNodo(matriz.attrib['nombre'])
listamad.mat = ListaNueva
print('\nLista de Matriz')
listaClases.mostrar()