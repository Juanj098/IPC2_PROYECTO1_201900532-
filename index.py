import xml.sax
import os

from organismo import organismos
from organismo import muestras
from listaD_orga import listaDa_orga
#listas
from list_A import listaDoble_Aposx
from list_A import listaDoble_Aposy
from list_B import listaDoble_Bposx
from list_B import listaDoble_Bposy
from list_C import listaDoble_Cposx
from list_C import listaDoble_Cposy
from list_D import listaDoble_Dposx
from list_D import listaDoble_Dposy

Doc = ""

lista_dobleOrga = listaDa_orga()    
Ax = listaDoble_Aposx()
Ay = listaDoble_Aposy()
Bx = listaDoble_Bposx()
By = listaDoble_Bposy()
Cx = listaDoble_Cposx()
Cy = listaDoble_Cposy()
Dx = listaDoble_Dposx()
Dy = listaDoble_Dposy()
class orga(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""

        self.listaorganismos = None
        #listado organismos ->
        self.organismo = ""
        self.codigo = ""
        self.name = ""

        self.listamuestras = None
        #listado muestras ->
        self.descrip = ""
        self.fil = ""
        self.col = ""

        self.listaC_Vivas = None
        #listado celdas vivas ->
        self.posx = ""
        self.posy = ""
        self.codOrg = ""

    def startElement(self, tag, attrs):
        self.current = tag
        if tag == "listaOrganismos":
            self.listaorganismos = lista_dobleOrga
           
        elif tag == "listadoCeldasVivas":
            print(f"--celdas vivas--")
            

    def characters(self, content):
        if self.current == "codigo":
            self.codigo = content
        elif self.current == "nombre":
            self.name = content
        elif self.current == "descripcion":
            self.descrip = content
        elif self.current == "filas":
            self.fil = content
        elif self.current == "columnas":
            self.col = content
        elif self.current == "fila":
            self.posx = content
        elif self.current == "columna":
            self.posy = content
        elif self.current == "codigoOrganismo":
            self.codOrg = content

    def endElement(self, tag):
        if tag == "organismo":
            orga=organismos(self.codigo,self.name)
            self.listaorganismos.agregarF(orga)
        elif tag == "muestra":
            print(f"--listado Muestras--")
            print(f"codigo: {self.codigo}")
            print(f"descripcion: {self.descrip}")
            print(f"filas: {self.fil}")
            print(f"columnas: {self.col}")
        elif tag == "celdaViva":
            if self.codOrg == "OA":
                Ax.agregar(self.posx)
                Ay.agregar(self.posy)
            elif self.codOrg == "OB":
                Bx.agregar(self.posx)
                By.agregar(self.posy) 
            elif self.codOrg == "OC":
                Cx.agregar(self.posx)
                Cy.agregar(self.posy)
            elif self.codOrg == "OD":
                Dx.agregar(self.posx)
                Dy.agregar(self.posy)
            mues = muestras(self.codOrg, self.posx, self.posy)
        self.current = ""
  

print("<------------------------------------>")
print("1. ingresar documento"                 )
print("2. Ver muestras                       ")
print("3. Ingresar organismo"                 )
print("4. Salir"                              )
print("<------------------------------------>")
opc = input("Ingrese opcion:")
while opc != "4":
    if opc == "1":
        Doc = input("Ingrese Documento -> ")
        handler = orga()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(Doc)
    elif opc =="2":
        cadena = '''
            digraph G{
            node [shape = plaintext];
            rankdir=LR;\n\n
        '''
        print(cadena)
    elif opc =="3":
        pass
    elif opc =="4":
        pass
    else:
        print("opcion no disponible :)")
    print("<------------------------------------>")
    print("1. ingresar documento"                 )
    print("2. Ver muestras                       ")
    print("3. Ingresar organismo"                 )
    print("4. Salir"                              )
    print("<------------------------------------>")
    opc = input("Ingrese opcion:")    







