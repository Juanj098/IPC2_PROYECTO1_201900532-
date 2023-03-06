from NodoEncabezado import NodoEncabezado

class ListaEncabezado:

    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None


    def insert(self,nuevo:NodoEncabezado):
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else: 
            if nuevo.id < self.primero.id:
                nuevo.sig = self.primero
                self.primero.ant = nuevo
                self.primero = nuevo
            elif nuevo.id > self.ultimo.id:
                nuevo.ant = self.ultimo
                self.ultimo.sig = nuevo
                self.ultimo = nuevo
            else:
                actual = self.primero
                while actual != None:
                    if nuevo.id < actual.id:
                        nuevo.sig = actual
                        nuevo.ant = actual.ant
                        actual.ant.sig = nuevo
                        actual.ant = nuevo
                        break
                    actual = actual.sig

        
    def buscar(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.sig
        return None

    def mostrar(self):
        actual = self.primero
        while actual != None:
            print(actual.id) 
            actual = actual.sig