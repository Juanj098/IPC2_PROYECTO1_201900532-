class organismos():
    def __init__(self, codi, nam):
        self.codi = codi
        self.nam = nam

    def __str__(self):
        return f"codigo de organismo -> {self.codi}; nombre de organismo -> {self.nam}"


class muestras():
    def __init__(self, code,x,y):
        self.code = code
        self.x = x
        self.y = y
    
    def __str__(self) :
        return f"codigo organismo -> {self.code}; posicion x -> {self.x}; posicion y -> {self.y}"
    
