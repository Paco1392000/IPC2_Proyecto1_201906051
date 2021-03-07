from tkinter import filedialog
from Doble.ListaDoble import ListaDoble
from Doble.ListaSimple import ListaSimple
import xml.etree.cElementTree as ET

#parsear xml para obtener clases de las cosas
tree = ET.parse('Matriz.xml')
root = tree.getroot()

#declarar listas
ima = ListaSimple()

#Recorrer lista de elementos XML
for elemento in root:
    for subelemento in elemento:
        ima.insertar(subelemento.text, "")

listaClases = ListaDoble()
#Clases = etree.xpath('//clase')
for clase in root:
    listaClases.insertar(clase.attrib['clase'], clase.attrib['n'], clase.attrib['m'])

print('lista de clases de cosas sin cosas')
listaClases.mostrar()
clase_mam = listaClases.getNodo('ejempo')
clase_mam.ima = ima
print('\nLista de clases de algo')
listaClases.mostrar()