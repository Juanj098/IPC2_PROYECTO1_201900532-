class Nodo():
    
    def __init__(self,dato, ant = None, sig = None):
        self.dato = dato
        self.ant = ant
        self.sig = sig
    
class listaDoble_Cposx(object):

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0
    
    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.ant = self.ultimo
            self.ultimo.sig = nodo
            self.ultimo = nodo
        self.len += 1
    
    def iterar(self):
        actual = self.primero
        while actual:
            dato = actual.dato
            actual = actual.sig
            yield dato

class listaDoble_Cposy(object):
   
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.len = 0
    
    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else:
            nodo.ant = self.ultimo
            self.ultimo.sig = nodo
            self.ultimo = nodo
        self.len += 1
    
    def iterar(self):
        actual = self.primero
        while actual:
            dato = actual.dato
            actual = actual.sig
            yield dato