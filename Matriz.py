from NodoEncabezado import NodoEncabezado
from ListaEncabezado import ListaEncabezado
from NodoInterno import NodoInterno
import os

class matriz:
    def __init__(self) -> None:
        self.filas = ListaEncabezado()
        self.columnas = ListaEncabezado()
    
    def insertar(self, x, y, valor):
        nuevo = NodoInterno(x,y,valor)

        if self.filas.buscar(x) == None:
            self.filas.insert(NodoEncabezado(x))
        if self.columnas.buscar(y) == None:
            self.columnas.insert(NodoEncabezado(y))

        fila = self.filas.buscar(x)
        col = self.columnas.buscar(y)

        actual = fila.acceso
        while actual != None:
            if actual.col == y:
                actual.valor = valor
                return
            actual = actual.der

        actual == col.acceso
        while actual != None:
            if actual.fila == x:
                actual.valor = valor
                return
            actual = actual.abajo
        
        if fila.acceso == None:
            fila.acceso = nuevo
        else:
            if nuevo.col < fila.acceso.col:
                nuevo.der = fila.acceso
                fila.acceso.izq = nuevo
                fila.acceso = nuevo
            elif nuevo.col > fila.acceso.col:
                actual = fila.acceso
                while actual.der != None:
                    actual = actual.der
                actual.der = nuevo
                nuevo.izq = actual
            else:
                actual = fila.acceso
                while actual.der != None:
                    if nuevo.col < actual.der.col:
                        nuevo.der = actual.der
                        nuevo.izq = actual
                        actual.der.izq = nuevo
                        actual.der = nuevo
                        break
                    actual = actual.der
                
        if col.acceso == None:
            col.acceso = nuevo
        else:
            if nuevo.fila < col.acceso.fila:
                nuevo.abajo = col.acceso
                col.acceso.arriba = nuevo
                col.acceso = nuevo
            elif nuevo.fila > col.acceso.fila:
                actual = col.acceso
                while actual.abajo != None:
                    actual = actual.abajo
                actual.abajo = nuevo
                nuevo.arriba = actual
            else:
                actual = col.acceso
                while actual.abajo != None:
                    if nuevo.fila < actual.abajo.fila:
                        nuevo.abajo = actual.abajo 
                        nuevo.arriba = actual
                        actual.abajo.arriba = nuevo
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

    def search(self, x, y):
        fila = self.filas.buscar(x)
        if fila == None:
            return None
        else:
            actual = fila.acceso
            while actual != None:
                if actual.col == y:
                    return actual
                actual = actual.der
            return None
        
    def recorrer(self):
        actual = self.filas.primero
        if actual == None:
            print("lista vacia")
        while actual != None:
            actual2 = actual.acceso
            print(f'fila: {str(actual.id)}')
            while actual2 != None:
                print(actual2.valor)
                actual2 = actual2.der
            actual = actual.sig
        
    def buscar_val(self, valor):
        actual = self.filas.primero
        while actual != None:
            actual2 = actual.acceso
            while actual2 != None:
                if actual2.valor == valor:
                    return actual2
                actual2 = actual2.der
            actual = actual.sig
        return None

    

    def graficar(self, Tfil, Tcol):
        if self.filas.primero == None:
            return
        if self.columnas.primero == None:
            return

        cadena = ""
        cadena += '''
        Digraph main {
        \tgraph[pad="0.5", nodesep="0.5", ranksep="2"]
        \tnode [shape = plain]
        \trankdir=LR;
        \tMatriz [
        '''
        cadena += "\tlabel=<<table border='0' cellborder='1' cellspacing='0'>\n"
        cadena += "\t\t<tr>\n"
        cadena += "\t\t<td></td>\n"
        actual = self.columnas.primero
        for x in range(Tfil):
            if x <= 8:
                cadena += f"\t\t<td>0{str(x+1)}</td>\n"
            else:
                cadena += f"\t\t<td>{str(x+1)}</td>\n"
        cadena += "\t\t</tr>\n"

        for y in range(Tcol):
            cadena +="\t\t<tr>\n"
            cadena += f"\t\t<td>{str(y+1)}</td>\n"
            for x in range (Tfil):
                Bx = self.filas.buscar(x)
                By = self.columnas.buscar(y)
                res = self.search(Bx,By)
                if res != None:
                    cadena += "\t\t<td>x</td>\n"
                else:
                    cadena += "\t\t<td></td>\n"                    
            cadena +="\t\t</tr>\n"

        cadena += "\t</table>>];\n"
        cadena += "}"
        return cadena


    
    def return_Id(self):
        actual = self.filas.primero
        while actual != None:
            print(actual.id)
            aux = self.columnas.primero
            while aux != None:
                temp = self.search(actual.id, aux.id)
                if temp != None:
                    print("->",temp.valor)
                aux = aux.sig
            actual = actual.sig














                