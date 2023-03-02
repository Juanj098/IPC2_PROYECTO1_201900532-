import xml.sax
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

Doc = "DatosMarte.xml"

lista_dobleOrga = listaDa_orga()    
Ax = listaDoble_Aposx()
Ay = listaDoble_Aposy()
Bx = listaDoble_Bposx()
By = listaDoble_Bposy()
Cx = listaDoble_Cposx()
Cy = listaDoble_Cposy()
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
                print(f"codigo organismo: {self.codOrg}")
                Ax.agregar(self.posx)
                Ay.agregar(self.posy)
            elif self.codOrg == "OB":
                print(f"codigo organismo: {self.codOrg}") 
                Bx.agregar(self.posx)
                By.agregar(self.posy) 
            elif self.codOrg == "OC":
                print(f"codigo organismo: {self.codOrg}")
                Cx.agregar(self.posx)
                Cy.agregar(self.posy)
            elif self.codOrg == "OD":
                print(f"codigo organismo: {self.codOrg}")              
            mues = muestras(self.codOrg, self.posx, self.posy)
        self.current = ""
  
handler = orga()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(Doc)

print("-------------------")
for x in Ax.iterar():
    print(f"x -> {x}")

for y in Ay.iterar():
    print(f"y -> {y}")
    
for xy in range(Ay.leng()):
    print(Ay.leng(), " ; " , Ax.leng(), " ; ", xy)
    print(f"x -> {Ax.__getItemAx__(xy)}, y -> {Ay.__getItemAy__(xy)}")

# print(f"x -> {Ax.__getItemAx__(0)}, y -> {Ay.__getItemAy__(0)}")
# print(f"x -> {Ax.__getItemAx__(1)}, y -> {Ay.__getItemAy__(1)}")

print(Ay.leng(), " :" , Ax.leng())

print("-------------------")

for x in Bx.iterar():
    print(f"x -> {x}")

for y in By.iterar():
    print(f"y -> {y}")
print("-------------------")

print("-------------------")
for x in Cx.iterar():
    print(f"x -> {x}")

for y in Cy.iterar():
    print(f"y -> {y}")

print("-------------------")










