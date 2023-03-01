import xml.sax
from organismo import organismos
from organismo import muestras

Doc = "DatosMarte.xml"
    
 
listorg=[]
listmuestras=[]
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
            print(f"--listado organismo--")
           

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
            listorg.append(orga)
        elif tag == "muestra":
            print(f"--listado Muestras--")
            print("<----------------->")
            print(f"codigo: {self.codigo}")
            print(f"descripcion: {self.descrip}")
            print(f"filas: {self.fil}")
            print(f"columnas: {self.col}")
        elif tag == "celdaViva":
            mues = muestras(self.codOrg, self.posx, self.posy)
            listmuestras.append(mues)
        self.current = ""
  
handler = orga()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(Doc)

for organism in listorg:
    print(organism.__str__()) 
    print("-------------------")

for muestra in listmuestras:
    print(muestra.__str__())
    print("-------------------")








