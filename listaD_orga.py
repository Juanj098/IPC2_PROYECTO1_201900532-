class Nodo():
    def __init__(self, dato, sig = None, ant = None):
        self.dato = dato
        self.sig = sig
        self.ant = ant

class listaDa_orga(object):
    def __init__(self) :
        self.primero = None
        self.ultimo = None
        self.len = 0
    
    def vacia(self):
        return self.primero == None
    
    def agregarF(self,dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
            self.ultimo = nodo
        else: 
            nodo.ant = self.ultimo
            self.ultimo.sig = nodo
            self.ultimo = nodo
        self.len+=1
    
    def iterar(self):
        actual = self.primero
        while actual:
            dato = actual.dato
            actual = actual.sig
            yield dato

    def testfunc(self):
        return("esto es un test")