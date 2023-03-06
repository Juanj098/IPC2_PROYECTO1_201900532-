class NodoInterno:   
    def __init__(self, posx = None, posy = None, valor = None) -> None:
         self.fila = posx
         self.col = posy 
         self.valor = valor

         self.arriba = None
         self.abajo = None
         self.der = None
         self.izq = None 