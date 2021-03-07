from tkinter import filedialog
from ListaDoble import ListaDoble
from ListaSimple import ListaSimple
import xml.etree.cElementTree as ET

#parsear xml para obtener clases de las cosas
tree = ET.parse('Matriz.xml')
root = tree.getroot()

#declarar listas
ListaNueva = ListaSimple()

#Recorrer lista de elementos XML
for elemento in root:
    if elemento.attrib['nombre'] != '':
        for subelemento in elemento:
            ListaNueva.insertar(subelemento.text, subelemento.attrib['x'], subelemento.attrib['y'])
            
listaClases = ListaDoble()
#Clases = etree.xpath('//clase')
for matriz in root:
    listaClases.insertar(matriz.attrib['nombre'], matriz.attrib['n'], matriz.attrib['m'])

print('lista de clases de cosas sin cosas')
listaClases.mostrar()
listamad = listaClases.getNodo('Ejemplo')
listamad.algo = ListaNueva
print('\nLista de Matriz')
listaClases.mostrar()
ListaNueva.mostrar()