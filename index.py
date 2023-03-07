import xml.sax
import os

os.system('cls')

from organismo import organismos
from organismo import matrix
from organismo import list_orga
from listaD_orga import listaDa_orga
from Matriz import matriz


Doc = ""
xy = {}
colors=["#ffc700","#00d278","#0082f7","#ea449e","#10c7dc","#ff0000","#00854c","#11dcf5","#ffe748","#af8b69","#e8e7f0","#f955ff","#91a7d2","#fb6e42","#eacb7c","#5b3347","#ffa8d2"]
lista_dobleOrga = listaDa_orga() 
matriz = matriz()
datos_orga = organismos
datosM = matrix 

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
            self.listaorganismos = list_orga
           
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
                if self.codigo != None:
                    orga=organismos(self.codigo,self.name)
                    self.listaorganismos.append(orga)
        elif tag == "muestra":
            print(f"--listado Muestras--")
            print(f"codigo: {self.codigo}")
            print(f"descripcion: {self.descrip}")
            datx = matrix(self.fil, self.col)
            xy["x"] = self.fil
            xy["y"] = self.col
        elif tag == "celdaViva":
            matriz.insertar(self.posx, self.posy, self.codOrg)
        self.current = ""
  

print("<------------------------------------>")
print("1. ingresar documento"                 )
print("2. Ver muestras                       ")
print("3. Ingresar organismo"                 )
print("4. Analisis muestra"                   )
print("5. Salir"                              )
print("<------------------------------------>")
opc = input("Ingrese opcion:")
os.system('cls')

while opc != "5":
    if opc == "1": #ingresar Doc
        Doc = input("Ingrese Documento -> ")
        handler = orga()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse(Doc)
    elif opc =="2": #ver muestras de Doc. forma grafica
        for r in range(len(list_orga)):
            list_orga[r].asigColor(colors[r])

        matriz.graficar(int(xy.get("x")),int(xy.get("y")))

    elif opc =="3": #ingresar un nuevo organismo
        x = input("x -> ")
        y = input("y -> ")
        codi = input("Codig -> ")
        matriz.insertar(x,y,codi)
        matriz.graficar(int(xy.get("x")),int(xy.get("y")))

    elif opc =="4": #Analisis muestras
        pass
    elif opc =="5":#salida
        pass
    else:
        print("opcion no disponible :)")
    print("<------------------------------------>")
    print("1. ingresar documento"                 )
    print("2. Ver muestras                       ")
    print("3. Ingresar organismo"                 )
    print("4. Analisis muestra"                   )
    print("5. Salir"                              )
    print("<------------------------------------>")
    opc = input("Ingrese opcion:")    
    os.system('cls')







