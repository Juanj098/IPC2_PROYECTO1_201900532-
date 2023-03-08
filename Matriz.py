from NodoEncabezado import NodoEncabezado
from ListaEncabezado import ListaEncabezado
from NodoInterno import NodoInterno
from organismo import list_orga

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
        digraph main {
        \tgraph[pad="0.5", nodesep="0.5", ranksep="2"]
        \tnode [shape = plain]
        \trankdir=LR;
        \tMatriz [
        '''
        cadena += "\tlabel=<<table border='0' cellborder='1' cellspacing='0'>\n"
        cadena += "\t<tr>\n"
        cadena += "\t\t<td></td>\n"
        actual = self.columnas.primero
        for x in range(Tfil + 1):
            if x <= 9:
                cadena += f"\t\t<td> 0{str(x)} </td>\n"
            else:
                cadena += f"\t\t<td> {str(x)} </td>\n"
        cadena += "\t</tr>\n"

        for y in range(Tcol + 1):
            cadena += "\t<tr>\n"
            cadena += f"\t\t<td>{y}</td>\n"
            for x in range(Tfil + 1):
                temp = self.search(str(x),str(y))
                if temp != None:
                    for z in range(len(list_orga)):
                        if temp.valor == list_orga[z].returnCodi():
                            colorss = list_orga[z].returnColor()
                            cadena += f"\t\t<td bgcolor= '{colorss}'>{temp.valor}</td>\n"
                else:
                    cadena += "\t\t<td></td>\n"
            cadena += "\t</tr>\n"           
        cadena += "\t</table>>];\n"
        cadena += "}"
        with open('Matriz.dot','w',encoding="utf-8") as docu:
            docu.write(cadena)
            docu.close()
        os.system("dot -Tpng Matriz.dot -o Matriz.png")
        # return cadena


    
    def return_Id(self):
        actual = self.filas.primero
        while actual != None:
            print(type(actual.id))
            aux = self.columnas.primero
            while aux != None:
                # temp = self.search(actual.id, aux.id)
                # if temp != None:
                #     print("->",temp.valor)
                if aux and actual != None:
                    print(f"-> {actual.id}... -> {aux.id}")
                aux = aux.sig
            actual = actual.sig


    def analisis_O(self, x,y):
        temp = self.search(str(x),str(y))
        if temp != None:
            w_i = int(x)-1
            w_d = int(x)+1
            w_ar = int(y)-1
            W_ab = int(y)+1
            temp_iz = self.search(str(w_i),str(y))
            temp_der= self.search(str(w_d),str(y))
            temp_ar = self.search(str(x),str(w_ar))
            temp_ab = self.search(str(x),str(W_ab))
            temp_DIS = self.search(str(w_i),str(w_ar))
            temp_DII = self.search(str(w_i),str(W_ab))
            temp_DDS = self.search(str(w_d),str(w_ar))
            temp_DDI = self.search(str(w_d),str(W_ab))
            if temp_iz != None and temp_der != None:  #izquierda derecha
                if temp_iz.valor == temp_der.valor:
                    return "Prospera"
                else:
                    return "No prospera"
            elif temp_ar != None and temp_ab != None: #arriba abajo 
                if temp_ar.valor == temp_ab.valor:
                    return "Prospera"
                else:
                    return "No prospera"
            elif temp_DIS != None and temp_DDI != None:
                if temp_DIS.valor == temp_DDI.valor:
                    return "Prospera"
                else:
                    return "No prospera"
            elif temp_DDS != None and temp_DII != None:
                if temp_DDS.valor == temp_DII.valor:
                    return "Prospera"
                else:
                    return "No prosperar"
            else:
                return "No prospera"
        else:
            return "Organismo no encontrado"











                