list_orga = []

class organismos:
    def __init__(self, codi, nam):
        self.codi = codi
        self.nam = nam
        self.color = None
    def __str__(self):
        return f"{self.codi}; {self.nam}; {self.color}"

    def rec(self):
        return f"color -> {self.color}, codigo ->{self.codi}"
    
    def asigColor(self,color):
       self.color = color

    def returnColor(self):
        return self.color
    
    def returnCodi(self):
        return self.codi
    
class muestras:
    def __init__(self, code,x,y):
        self.code = code
        self.x = x
        self.y = y
    
    def __str__(self) :
        return f"codigo organismo -> {self.code}; posicion x -> {self.x}; posicion y -> {self.y}"
    

class matrix:
    def __init__(self, fils, cols) -> None:
        self.x = fils
        self.y = cols
    
    def retornaX(self,):
        return self.x