from list_A import Nodo

class listaDoble_Dposx(object):

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
    
    def leng(self):
        return self.len
    
    def __getItemDx__(self,indice):
        if indice >= 0 and indice < self.len:
            actual = self.primero
            for _ in range(indice):
                actual = actual.sig
            return actual.dato 
        else:
            print("indice no valido")

class listaDoble_Dposy(object):
   
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
    
    def leng(self):
        return self.len
    
    def __getItemDy__(self,indice):
        if indice >= 0 and indice < self.len:
            actual = self.primero
            for _ in range(indice):
                actual = actual.sig
            return actual.dato 
        else:
            print("indice no valido")