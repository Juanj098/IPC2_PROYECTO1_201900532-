class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        self.ant = None

class listaD_muestras():
    def __init__(self) :
        self.primero = None
        self.ultimo = None
        self.len = 0
    
    def vacia(self):
        return self.primero == None
    
    def agregarF(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.sig = Nodo(dato)
            self.ultimo.ant == aux
        self.len += 1 
    
    def agregarI(self, dato):
        if self.vacia():
            self.primero= self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.sig = self.primero
            self.primero.ant = None
            self.primero = aux
        self.len += 1
    
    def recorrer_ini(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.sig
    
    def recorrer_fin(self):
        aux = self.ultimo
        while aux != None:
            print(aux.dato)
            aux = aux.ant 
    
    def size(self):
        return self.len

    def eliminar_ini(self):
        if self.vacia():
            print("lista vacia")
        elif self.primero.sig == None:
            self.primero = self.ultimo = None
            self.len = 0
        else:
            self.primero = self.primero.sig
            self.primero.ant = None
            self.size -= 1
    def eliminar_fin(self):
        if self.vacia():
            print("lista vacia")
        elif self.ultimo.sig == None:
            self.primero = self.ultimo = None
            self.len = 0
        else:
            self.ultimo = self.ultimo.ant
            self.ultimo.sig = None
            self.len -= 1